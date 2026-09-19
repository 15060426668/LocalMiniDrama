const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const USER_AGENT =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36";

function usage() {
  console.error("Usage: node capture_douyin_profiles.cjs <output-dir> <url> [url ...]");
  process.exit(2);
}

function safeName(index) {
  return `creator-${String(index + 1).padStart(2, "0")}`;
}

async function captureProfile(context, url, outputDir, index) {
  const label = safeName(index);
  const profileDir = path.join(outputDir, label);
  fs.mkdirSync(profileDir, { recursive: true });

  const page = await context.newPage();
  const responses = [];

  page.on("response", async (response) => {
    const responseUrl = response.url();
    const contentType = response.headers()["content-type"] || "";
    if (!/aweme|user|profile|post|feed/i.test(responseUrl) || !/json|text/i.test(contentType)) {
      return;
    }

    try {
      const body = await response.text();
      if (body.length > 5_000_000) return;
      responses.push({
        url: responseUrl,
        status: response.status(),
        contentType,
        body,
      });
    } catch {
      // Streaming and canceled responses do not provide a stable body.
    }
  });

  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await page.waitForTimeout(8_000);

  const resolvedUrl = page.url();
  const secUidMatch = resolvedUrl.match(/\/share\/user\/([^?]+)/);
  if (secUidMatch) {
    const desktopUrl = `https://www.douyin.com/user/${secUidMatch[1]}`;
    await page.goto(desktopUrl, { waitUntil: "domcontentloaded", timeout: 60_000 });
    await page.waitForTimeout(8_000);
  }

  for (let step = 0; step < 14; step += 1) {
    await page.mouse.wheel(0, 1500);
    await page.waitForTimeout(900);
  }

  const snapshot = await page.evaluate(() => {
    const links = [...document.querySelectorAll("a[href]")]
      .map((element) => ({
        href: element.href,
        text: (element.innerText || element.getAttribute("aria-label") || "")
          .replace(/\s+/g, " ")
          .trim(),
      }))
      .filter((item) => item.href.includes("douyin.com"));

    return {
      title: document.title,
      url: location.href,
      bodyText: (document.body?.innerText || "").slice(0, 500_000),
      links,
    };
  });

  await page.screenshot({
    path: path.join(profileDir, "profile-full.png"),
    fullPage: true,
  });
  fs.writeFileSync(path.join(profileDir, "profile.html"), await page.content(), "utf8");
  fs.writeFileSync(
    path.join(profileDir, "snapshot.json"),
    JSON.stringify(snapshot, null, 2),
    "utf8",
  );
  fs.writeFileSync(
    path.join(profileDir, "network-responses.json"),
    JSON.stringify(responses, null, 2),
    "utf8",
  );

  console.log(
    JSON.stringify({
      label,
      requestedUrl: url,
      resolvedUrl: snapshot.url,
      title: snapshot.title,
      linkCount: snapshot.links.length,
      capturedResponses: responses.length,
    }),
  );
  await page.close();
}

async function main() {
  const [, , outputDirArg, ...urls] = process.argv;
  if (!outputDirArg || urls.length === 0) usage();

  const outputDir = path.resolve(outputDirArg);
  fs.mkdirSync(outputDir, { recursive: true });

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: [
      "--disable-blink-features=AutomationControlled",
      "--disable-dev-shm-usage",
      "--no-first-run",
    ],
  });
  const context = await browser.newContext({
    locale: "zh-CN",
    timezoneId: "Asia/Shanghai",
    userAgent: USER_AGENT,
    viewport: { width: 1440, height: 1200 },
  });

  try {
    for (let index = 0; index < urls.length; index += 1) {
      await captureProfile(context, urls[index], outputDir, index);
    }
  } finally {
    await context.close();
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
