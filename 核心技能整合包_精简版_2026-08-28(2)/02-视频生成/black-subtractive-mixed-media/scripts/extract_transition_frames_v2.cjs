const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");
const sharp = require("sharp");

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PAGE_URL = "https://local-video.invalid/index.html";
const VIDEO_URL = "https://local-video.invalid/reference.mp4";

async function seek(page, time) {
  await page.evaluate(async (target) => {
    const video = document.querySelector("video");
    if (Math.abs(video.currentTime - target) < 0.001 && video.readyState >= 2) return;
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error(`seek timeout ${target}`)), 5000);
      video.addEventListener("seeked", () => {
        clearTimeout(timeout);
        resolve();
      }, { once: true });
      video.currentTime = target;
    });
  }, time);
}

async function metricsAt(page, time) {
  await seek(page, time);
  return page.evaluate(() => {
    const video = document.querySelector("video");
    const canvas = document.querySelector("canvas");
    canvas.width = 160;
    canvas.height = Math.max(1, Math.round(160 * video.videoHeight / video.videoWidth));
    const context = canvas.getContext("2d", { willReadFrequently: true });
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const rgba = context.getImageData(0, 0, canvas.width, canvas.height).data;
    const gray = new Uint8Array(rgba.length / 4);
    let brightness = 0;
    let black = 0;
    let bright = 0;
    for (let source = 0, target = 0; source < rgba.length; source += 4, target += 1) {
      const value = Math.round(
        rgba[source] * 0.299 + rgba[source + 1] * 0.587 + rgba[source + 2] * 0.114,
      );
      gray[target] = value;
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

async function saveFrame(page, time, outputPath) {
  await seek(page, time);
  const dataUrl = await page.evaluate(() => {
    const video = document.querySelector("video");
    const canvas = document.querySelector("canvas");
    canvas.width = 960;
    canvas.height = Math.max(1, Math.round(960 * video.videoHeight / video.videoWidth));
    const context = canvas.getContext("2d");
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL("image/jpeg", 0.88);
  });
  fs.writeFileSync(outputPath, Buffer.from(dataUrl.split(",", 2)[1], "base64"));
}

function chooseCuts(timeline, threshold, minGap, limit) {
  const candidates = timeline.filter((item, index) => {
    if (item.difference < threshold) return false;
    const left = timeline[index - 1]?.difference ?? -1;
    const right = timeline[index + 1]?.difference ?? -1;
    return item.difference >= left && item.difference >= right;
  });
  const selected = [];
  for (const item of candidates.sort((left, right) => right.difference - left.difference)) {
    if (selected.every((chosen) => Math.abs(chosen.time - item.time) >= minGap)) {
      selected.push(item);
      if (selected.length >= limit) break;
    }
  }
  return selected.sort((left, right) => left.time - right.time);
}

async function contactSheet(items, outputPath) {
  if (!items.length) return;
  const columns = 5;
  const tileWidth = 280;
  const tileHeight = 190;
  const rows = Math.ceil(items.length / columns);
  const layers = [];
  for (let index = 0; index < items.length; index += 1) {
    const item = items[index];
    const left = (index % columns) * tileWidth;
    const top = Math.floor(index / columns) * tileHeight;
    const image = await sharp(item.path)
      .resize(tileWidth - 8, tileHeight - 32, { fit: "contain", background: "#111" })
      .jpeg({ quality: 84 })
      .toBuffer();
    const label = Buffer.from(
      `<svg width="${tileWidth}" height="28"><rect width="100%" height="100%" fill="#111"/><text x="8" y="19" fill="#fff" font-size="15" font-family="Arial">${item.time.toFixed(2)}s</text></svg>`,
    );
    layers.push({ input: image, left: left + 4, top: top + 4 });
    layers.push({ input: label, left, top: top + tileHeight - 28 });
  }
  await sharp({
    create: {
      width: columns * tileWidth,
      height: rows * tileHeight,
      channels: 3,
      background: "#111",
    },
  }).composite(layers).jpeg({ quality: 90 }).toFile(outputPath);
}

async function extract(browser, videoPath, outputDir, sampleStep, analysisStep) {
  fs.mkdirSync(outputDir, { recursive: true });
  const samplesDir = path.join(outputDir, "samples");
  const cutsDir = path.join(outputDir, "cuts");
  fs.mkdirSync(samplesDir, { recursive: true });
  fs.mkdirSync(cutsDir, { recursive: true });

  const context = await browser.newContext();
  const page = await context.newPage();
  await page.route(PAGE_URL, (route) => route.fulfill({
    contentType: "text/html",
    body: `<video muted preload="auto" src="${VIDEO_URL}"></video><canvas></canvas>`,
  }));
  await page.route(VIDEO_URL, (route) => route.fulfill({
    path: videoPath,
    contentType: "video/mp4",
  }));
  await page.goto(PAGE_URL, { waitUntil: "load" });
  await page.waitForFunction(() => {
    const video = document.querySelector("video");
    return video && Number.isFinite(video.duration) && video.videoWidth > 0;
  });
  const info = await page.evaluate(() => {
    const video = document.querySelector("video");
    return { duration: video.duration, width: video.videoWidth, height: video.videoHeight };
  });
  const end = Math.max(0, info.duration - 0.04);

  await page.evaluate(() => { window.__previousGray = null; });
  const timeline = [];
  for (let time = 0; time <= end + 0.0001; time += analysisStep) {
    const point = Math.min(end, Number(time.toFixed(3)));
    timeline.push({ time: point, ...(await metricsAt(page, point)) });
  }
  const cutItems = chooseCuts(timeline, 0.12, 0.2, 12);

  const sampleTimes = [];
  for (let time = 0; time <= end + 0.0001; time += sampleStep) {
    sampleTimes.push(Math.min(end, Number(time.toFixed(3))));
  }
  if ((sampleTimes.at(-1) ?? -1) < end - 0.1) sampleTimes.push(end);

  const sampleItems = [];
  for (const time of sampleTimes) {
    const outputPath = path.join(samplesDir, `${time.toFixed(2).padStart(6, "0")}s.jpg`);
    await saveFrame(page, time, outputPath);
    sampleItems.push({ time, path: outputPath });
  }
  const cutImages = [];
  for (const item of cutItems) {
    const outputPath = path.join(cutsDir, `${item.time.toFixed(2).padStart(6, "0")}s.jpg`);
    await saveFrame(page, item.time, outputPath);
    cutImages.push({ time: item.time, path: outputPath });
  }

  const metadata = {
    video: videoPath,
    ...info,
    sampleStep,
    analysisStep,
    cutThreshold: 0.12,
    cutTimes: cutItems,
    sampleCount: sampleItems.length,
  };
  fs.writeFileSync(path.join(outputDir, "timeline.json"), JSON.stringify(timeline, null, 2));
  fs.writeFileSync(path.join(outputDir, "metadata.json"), JSON.stringify(metadata, null, 2));
  await contactSheet(sampleItems, path.join(outputDir, "contact-sheet-samples.jpg"));
  await contactSheet(cutImages, path.join(outputDir, "contact-sheet-cuts.jpg"));
  await context.close();
  console.log(JSON.stringify(metadata));
}

async function main() {
  const [, , videosRootArg, outputRootArg, sampleArg = "0.4", analysisArg = "0.2"] = process.argv;
  if (!videosRootArg || !outputRootArg) process.exit(2);
  const videosRoot = path.resolve(videosRootArg);
  const outputRoot = path.resolve(outputRootArg);
  const videos = [];
  for (const creator of fs.readdirSync(videosRoot, { withFileTypes: true })) {
    if (!creator.isDirectory()) continue;
    const creatorDir = path.join(videosRoot, creator.name);
    for (const fileName of fs.readdirSync(creatorDir).sort()) {
      if (fileName.toLowerCase().endsWith(".mp4")) {
        videos.push(path.join(creatorDir, fileName));
      }
    }
  }
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ["--disable-dev-shm-usage", "--no-first-run"],
  });
  try {
    for (const video of videos) {
      const relative = path.relative(videosRoot, video).replace(/\.mp4$/i, "");
      await extract(
        browser,
        video,
        path.join(outputRoot, relative),
        Number(sampleArg),
        Number(analysisArg),
      );
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
