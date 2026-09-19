const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");
const sharp = require("sharp");

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const VIDEO_URL = "https://local-video.invalid/reference.mp4";

function parseNumber(value, fallback) {
  const number = Number(value);
  return Number.isFinite(number) ? number : fallback;
}

function timestampName(time) {
  return `${time.toFixed(2).padStart(6, "0")}s.jpg`;
}

async function seek(page, time) {
  await page.evaluate(async (targetTime) => {
    const video = document.querySelector("video");
    if (Math.abs(video.currentTime - targetTime) < 0.001 && video.readyState >= 2) {
      return;
    }
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error(`Seek timeout at ${targetTime}`)), 5000);
      video.addEventListener(
        "seeked",
        () => {
          clearTimeout(timeout);
          resolve();
        },
        { once: true },
      );
      video.currentTime = targetTime;
    });
  }, time);
}

async function analyzeFrame(page, time) {
  await seek(page, time);
  return page.evaluate(() => {
    const video = document.querySelector("video");
    const canvas = document.querySelector("canvas");
    const width = 160;
    const height = Math.max(1, Math.round((video.videoHeight / video.videoWidth) * width));
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext("2d", { willReadFrequently: true });
    context.drawImage(video, 0, 0, width, height);
    const rgba = context.getImageData(0, 0, width, height).data;
    const gray = new Uint8Array(width * height);
    let brightness = 0;
    let black = 0;
    let bright = 0;
    for (let index = 0, pixel = 0; index < rgba.length; index += 4, pixel += 1) {
      const value = Math.round(
        rgba[index] * 0.299 + rgba[index + 1] * 0.587 + rgba[index + 2] * 0.114,
      );
      gray[pixel] = value;
      brightness += value;
      if (value <= 12) black += 1;
      if (value >= 220) bright += 1;
    }

    let difference = 0;
    if (window.__previousGray?.length === gray.length) {
      for (let index = 0; index < gray.length; index += 1) {
        difference += Math.abs(gray[index] - window.__previousGray[index]);
      }
      difference /= gray.length * 255;
    }
    window.__previousGray = gray;
    return {
      difference,
      brightness: brightness / gray.length,
      blackRatio: black / gray.length,
      brightRatio: bright / gray.length,
    };
  });
}

async function captureFrame(page, time, outputPath, outputWidth) {
  await seek(page, time);
  const dataUrl = await page.evaluate((width) => {
    const video = document.querySelector("video");
    const canvas = document.querySelector("canvas");
    const height = Math.max(1, Math.round((video.videoHeight / video.videoWidth) * width));
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext("2d");
    context.drawImage(video, 0, 0, width, height);
    return canvas.toDataURL("image/jpeg", 0.88);
  }, outputWidth);
  fs.writeFileSync(outputPath, Buffer.from(dataUrl.split(",", 2)[1], "base64"));
}

function selectCutTimes(timeline, threshold, minGap, maxCuts) {
  const localMaxima = timeline.filter((item, index) => {
    if (item.difference < threshold) return false;
    const previous = timeline[index - 1]?.difference ?? -1;
    const next = timeline[index + 1]?.difference ?? -1;
    return item.difference >= previous && item.difference >= next;
  });

  const selected = [];
  for (const candidate of localMaxima.sort((a, b) => b.difference - a.difference)) {
    if (selected.every((item) => Math.abs(item.time - candidate.time) >= minGap)) {
      selected.push(candidate);
      if (selected.length >= maxCuts) break;
    }
  }
  return selected.sort((a, b) => a.time - b.time);
}

async function makeContactSheet(frames, outputPath, columns = 5) {
  if (frames.length === 0) return;
  const tileWidth = 280;
  const tileHeight = 190;
  const rows = Math.ceil(frames.length / columns);
  const composites = [];

  for (let index = 0; index < frames.length; index += 1) {
    const item = frames[index];
    const left = (index % columns) * tileWidth;
    const top = Math.floor(index / columns) * tileHeight;
    const image = await sharp(item.path)
      .resize(tileWidth - 8, tileHeight - 32, {
        fit: "contain",
        background: "#111111",
      })
      .jpeg({ quality: 84 })
      .toBuffer();
    const label = Buffer.from(
      `<svg width="${tileWidth}" height="28"><rect width="100%" height="100%" fill="#111"/><text x="8" y="19" fill="#fff" font-size="15" font-family="Arial">${item.time.toFixed(2)}s</text></svg>`,
    );
    composites.push({ input: image, left: left + 4, top: top + 4 });
    composites.push({ input: label, left, top: top + tileHeight - 28 });
  }

  await sharp({
    create: {
      width: tileWidth * columns,
      height: tileHeight * rows,
      channels: 3,
      background: "#111111",
    },
  })
    .composite(composites)
    .jpeg({ quality: 90 })
    .toFile(outputPath);
}

async function extractVideo(browser, videoPath, outputDir, options) {
  fs.mkdirSync(outputDir, { recursive: true });
  const samplesDir = path.join(outputDir, "samples");
  const cutsDir = path.join(outputDir, "cuts");
  fs.mkdirSync(samplesDir, { recursive: true });
  fs.mkdirSync(cutsDir, { recursive: true });

  const context = await browser.newContext();
  const page = await context.newPage();
  await page.route(VIDEO_URL, async (route) => {
    await route.fulfill({ path: videoPath, contentType: "video/mp4" });
  });
  await page.setContent(
    `<video muted preload="auto" src="${VIDEO_URL}"></video><canvas></canvas>`,
    { waitUntil: "load" },
  );
  await page.waitForFunction(() => {
    const video = document.querySelector("video");
    return video && Number.isFinite(video.duration) && video.videoWidth > 0;
  });

  const videoInfo = await page.evaluate(() => {
    const video = document.querySelector("video");
    return {
      duration: video.duration,
      width: video.videoWidth,
      height: video.videoHeight,
    };
  });

  const safeEnd = Math.max(0, videoInfo.duration - 0.04);
  const timeline = [];
  await page.evaluate(() => {
    window.__previousGray = null;
  });
  for (let time = 0; time <= safeEnd + 0.0001; time += options.analysisStep) {
    const roundedTime = Math.min(safeEnd, Number(time.toFixed(3)));
    const metrics = await analyzeFrame(page, roundedTime);
    timeline.push({ time: roundedTime, ...metrics });
  }

  const sampleTimes = [];
  for (let time = 0; time <= safeEnd + 0.0001; time += options.sampleStep) {
    sampleTimes.push(Math.min(safeEnd, Number(time.toFixed(3))));
  }
  if (sampleTimes.at(-1) < safeEnd - 0.1) sampleTimes.push(safeEnd);

  const cutFrames = selectCutTimes(
    timeline,
    options.cutThreshold,
    options.minCutGap,
    options.maxCuts,
  );

  const sampleFrames = [];
  for (const time of sampleTimes) {
    const outputPath = path.join(samplesDir, timestampName(time));
    await captureFrame(page, time, outputPath, options.outputWidth);
    sampleFrames.push({ time, path: outputPath });
  }

  const cutImages = [];
  for (const item of cutFrames) {
    const outputPath = path.join(cutsDir, timestampName(item.time));
    await captureFrame(page, item.time, outputPath, options.outputWidth);
    cutImages.push({ time: item.time, path: outputPath });
  }

  fs.writeFileSync(
    path.join(outputDir, "timeline.json"),
    JSON.stringify(timeline, null, 2),
    "utf8",
  );
  const metadata = {
    video: videoPath,
    durationSeconds: videoInfo.duration,
    width: videoInfo.width,
    height: videoInfo.height,
    sampleStep: options.sampleStep,
    analysisStep: options.analysisStep,
    cutThreshold: options.cutThreshold,
    cutTimes: cutFrames,
    sampleCount: sampleFrames.length,
  };
  fs.writeFileSync(
    path.join(outputDir, "metadata.json"),
    JSON.stringify(metadata, null, 2),
    "utf8",
  );
  await makeContactSheet(sampleFrames, path.join(outputDir, "contact-sheet-samples.jpg"));
  await makeContactSheet(cutImages, path.join(outputDir, "contact-sheet-cuts.jpg"));
  await context.close();
  console.log(JSON.stringify(metadata));
}

async function main() {
  const [, , videosRootArg, outputRootArg, sampleStepArg, analysisStepArg] = process.argv;
  if (!videosRootArg || !outputRootArg) {
    console.error(
      "Usage: node extract_transition_frames.cjs <videos-root> <output-root> [sample-step] [analysis-step]",
    );
    process.exit(2);
  }

  const videosRoot = path.resolve(videosRootArg);
  const outputRoot = path.resolve(outputRootArg);
  const options = {
    sampleStep: parseNumber(sampleStepArg, 0.4),
    analysisStep: parseNumber(analysisStepArg, 0.1),
    cutThreshold: 0.12,
    minCutGap: 0.2,
    maxCuts: 12,
    outputWidth: 960,
  };
  const videoPaths = [];
  for (const creatorEntry of fs.readdirSync(videosRoot, { withFileTypes: true })) {
    if (!creatorEntry.isDirectory()) continue;
    const creatorDir = path.join(videosRoot, creatorEntry.name);
    for (const fileName of fs.readdirSync(creatorDir).sort()) {
      if (fileName.toLowerCase().endsWith(".mp4")) {
        videoPaths.push(path.join(creatorDir, fileName));
      }
    }
  }

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ["--disable-dev-shm-usage", "--no-first-run"],
  });
  try {
    for (const videoPath of videoPaths) {
      const relative = path.relative(videosRoot, videoPath);
      const outputDir = path.join(outputRoot, relative.replace(/\.mp4$/i, ""));
      await extractVideo(browser, videoPath, outputDir, options);
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
