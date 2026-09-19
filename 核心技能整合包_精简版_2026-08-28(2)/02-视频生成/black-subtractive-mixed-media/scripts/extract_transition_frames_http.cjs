const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { chromium } = require("playwright");
const sharp = require("sharp");

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
let currentVideo = null;

function startVideoServer() {
  const server = http.createServer((request, response) => {
    if (request.url === "/") {
      response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      response.end('<video muted preload="auto" src="/video.mp4"></video><canvas></canvas>');
      return;
    }
    if (request.url !== "/video.mp4" || !currentVideo) {
      response.writeHead(404);
      response.end();
      return;
    }

    const size = fs.statSync(currentVideo).size;
    const range = request.headers.range;
    if (!range) {
      response.writeHead(200, {
        "Accept-Ranges": "bytes",
        "Content-Length": size,
        "Content-Type": "video/mp4",
      });
      fs.createReadStream(currentVideo).pipe(response);
      return;
    }

    const match = range.match(/bytes=(\d*)-(\d*)/);
    const start = match?.[1] ? Number(match[1]) : 0;
    const end = match?.[2] ? Math.min(Number(match[2]), size - 1) : size - 1;
    response.writeHead(206, {
      "Accept-Ranges": "bytes",
      "Content-Length": end - start + 1,
      "Content-Range": `bytes ${start}-${end}/${size}`,
      "Content-Type": "video/mp4",
    });
    fs.createReadStream(currentVideo, { start, end }).pipe(response);
  });
  return new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", () => resolve(server));
  });
}

async function seek(page, time) {
  await page.evaluate(async (target) => {
    const video = document.querySelector("video");
    if (Math.abs(video.currentTime - target) < 0.001 && video.readyState >= 2) return;
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error(`seek timeout ${target}`)), 5000);
      video.addEventListener("seeked", () => {
        clearTimeout(timeout);
        requestAnimationFrame(() => requestAnimationFrame(resolve));
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
    canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL("image/jpeg", 0.88);
  });
  fs.writeFileSync(outputPath, Buffer.from(dataUrl.split(",", 2)[1], "base64"));
}

function chooseCuts(timeline) {
  const candidates = timeline.filter((item, index) => {
    if (item.difference < 0.12) return false;
    return item.difference >= (timeline[index - 1]?.difference ?? -1)
      && item.difference >= (timeline[index + 1]?.difference ?? -1);
  });
  const selected = [];
  for (const item of candidates.sort((left, right) => right.difference - left.difference)) {
    if (selected.every((chosen) => Math.abs(chosen.time - item.time) >= 0.2)) {
      selected.push(item);
      if (selected.length >= 12) break;
    }
  }
  return selected.sort((left, right) => left.time - right.time);
}

async function makeSheet(items, outputPath) {
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
      width: tileWidth * columns,
      height: tileHeight * rows,
      channels: 3,
      background: "#111",
    },
  }).composite(layers).jpeg({ quality: 90 }).toFile(outputPath);
}

async function extract(page, pageUrl, videoPath, outputDir, sampleStep, analysisStep) {
  currentVideo = videoPath;
  await page.goto(pageUrl, { waitUntil: "load" });
  await page.waitForFunction(() => {
    const video = document.querySelector("video");
    return video && Number.isFinite(video.duration) && video.videoWidth > 0;
  });
  const info = await page.evaluate(() => {
    const video = document.querySelector("video");
    return { duration: video.duration, width: video.videoWidth, height: video.videoHeight };
  });
  const end = Math.max(0, info.duration - 0.04);
  fs.mkdirSync(path.join(outputDir, "samples"), { recursive: true });
  fs.mkdirSync(path.join(outputDir, "cuts"), { recursive: true });

  await page.evaluate(() => { window.__previousGray = null; });
  const timeline = [];
  for (let time = 0; time <= end + 0.0001; time += analysisStep) {
    const point = Math.min(end, Number(time.toFixed(3)));
    timeline.push({ time: point, ...(await metricsAt(page, point)) });
  }
  const cuts = chooseCuts(timeline);

  const sampleTimes = [];
  for (let time = 0; time <= end + 0.0001; time += sampleStep) {
    sampleTimes.push(Math.min(end, Number(time.toFixed(3))));
  }
  if ((sampleTimes.at(-1) ?? -1) < end - 0.1) sampleTimes.push(end);

  const samples = [];
  for (const time of sampleTimes) {
    const outputPath = path.join(outputDir, "samples", `${time.toFixed(2).padStart(6, "0")}s.jpg`);
    await saveFrame(page, time, outputPath);
    samples.push({ time, path: outputPath });
  }
  const cutFrames = [];
  for (const item of cuts) {
    const outputPath = path.join(outputDir, "cuts", `${item.time.toFixed(2).padStart(6, "0")}s.jpg`);
    await saveFrame(page, item.time, outputPath);
    cutFrames.push({ time: item.time, path: outputPath });
  }

  const metadata = {
    video: videoPath,
    ...info,
    sampleStep,
    analysisStep,
    cutThreshold: 0.12,
    cutTimes: cuts,
    sampleCount: samples.length,
  };
  fs.writeFileSync(path.join(outputDir, "timeline.json"), JSON.stringify(timeline, null, 2));
  fs.writeFileSync(path.join(outputDir, "metadata.json"), JSON.stringify(metadata, null, 2));
  await makeSheet(samples, path.join(outputDir, "contact-sheet-samples.jpg"));
  await makeSheet(cutFrames, path.join(outputDir, "contact-sheet-cuts.jpg"));
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
      if (fileName.toLowerCase().endsWith(".mp4")) videos.push(path.join(creatorDir, fileName));
    }
  }

  const server = await startVideoServer();
  const port = server.address().port;
  const pageUrl = `http://127.0.0.1:${port}/`;
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ["--disable-dev-shm-usage", "--no-first-run"],
  });
  const page = await browser.newPage();
  try {
    for (const video of videos) {
      const relative = path.relative(videosRoot, video).replace(/\.mp4$/i, "");
      await extract(page, pageUrl, video, path.join(outputRoot, relative), Number(sampleArg), Number(analysisArg));
    }
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
