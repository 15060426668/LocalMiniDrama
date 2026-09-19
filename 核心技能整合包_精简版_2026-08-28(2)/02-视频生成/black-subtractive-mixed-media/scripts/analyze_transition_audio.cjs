const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

function selectPeaks(envelope, minGap = 0.18, limit = 12) {
  const candidates = envelope.filter((item, index) => {
    const left = envelope[index - 1]?.onset ?? -1;
    const right = envelope[index + 1]?.onset ?? -1;
    return item.onset >= left && item.onset >= right;
  });
  const selected = [];
  for (const item of candidates.sort((left, right) => right.onset - left.onset)) {
    if (selected.every((chosen) => Math.abs(chosen.time - item.time) >= minGap)) {
      selected.push(item);
      if (selected.length >= limit) break;
    }
  }
  return selected.sort((left, right) => left.time - right.time);
}

async function main() {
  const [, , videosRootArg, framesRootArg] = process.argv;
  if (!videosRootArg || !framesRootArg) process.exit(2);
  const videosRoot = path.resolve(videosRootArg);
  const framesRoot = path.resolve(framesRootArg);
  const videos = [];
  for (const creator of fs.readdirSync(videosRoot, { withFileTypes: true })) {
    if (!creator.isDirectory()) continue;
    const creatorDir = path.join(videosRoot, creator.name);
    for (const fileName of fs.readdirSync(creatorDir).sort()) {
      if (fileName.toLowerCase().endsWith(".mp4")) {
        videos.push({
          path: path.join(creatorDir, fileName),
          relative: path.join(creator.name, fileName.replace(/\.mp4$/i, "")),
        });
      }
    }
  }

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ["--autoplay-policy=no-user-gesture-required", "--no-first-run"],
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  let currentVideo = null;
  await page.route("https://audio-analysis.invalid/**", (route) => {
    const url = new URL(route.request().url());
    if (url.pathname === "/") {
      return route.fulfill({ contentType: "text/html", body: "<main>audio analysis</main>" });
    }
    return route.fulfill({ path: currentVideo, contentType: "video/mp4" });
  });
  await page.goto("https://audio-analysis.invalid/", { waitUntil: "load" });

  try {
    for (let index = 0; index < videos.length; index += 1) {
      const video = videos[index];
      currentVideo = video.path;
      const clipUrl = `https://audio-analysis.invalid/clip-${index}.mp4`;
      const result = await page.evaluate(async (url) => {
        const response = await fetch(url, { cache: "no-store" });
        const encoded = await response.arrayBuffer();
        const audioContext = new AudioContext();
        const decoded = await audioContext.decodeAudioData(encoded.slice(0));
        const stepSeconds = 0.02;
        const windowSize = Math.max(1, Math.round(decoded.sampleRate * stepSeconds));
        const channels = [];
        for (let channel = 0; channel < decoded.numberOfChannels; channel += 1) {
          channels.push(decoded.getChannelData(channel));
        }
        const envelope = [];
        let previousRms = 0;
        for (let start = 0; start < decoded.length; start += windowSize) {
          const end = Math.min(decoded.length, start + windowSize);
          let energy = 0;
          let count = 0;
          for (let sample = start; sample < end; sample += 1) {
            let value = 0;
            for (const channel of channels) value += channel[sample] || 0;
            value /= channels.length;
            energy += value * value;
            count += 1;
          }
          const rms = Math.sqrt(energy / Math.max(1, count));
          envelope.push({
            time: start / decoded.sampleRate,
            rms,
            onset: Math.max(0, rms - previousRms),
          });
          previousRms = rms;
        }
        await audioContext.close();
        return {
          duration: decoded.duration,
          sampleRate: decoded.sampleRate,
          channels: decoded.numberOfChannels,
          stepSeconds,
          envelope,
        };
      }, clipUrl);

      const output = {
        video: video.path,
        duration: result.duration,
        sampleRate: result.sampleRate,
        channels: result.channels,
        stepSeconds: result.stepSeconds,
        peaks: selectPeaks(result.envelope),
        envelope: result.envelope,
      };
      const outputDir = path.join(framesRoot, video.relative);
      fs.mkdirSync(outputDir, { recursive: true });
      fs.writeFileSync(
        path.join(outputDir, "audio-analysis.json"),
        JSON.stringify(output, null, 2),
        "utf8",
      );
      console.log(JSON.stringify({
        video: video.relative,
        duration: output.duration,
        peaks: output.peaks.slice(0, 5),
      }));
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
