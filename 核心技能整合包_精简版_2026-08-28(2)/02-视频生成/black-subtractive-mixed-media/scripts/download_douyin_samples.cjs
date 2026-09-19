const fs = require("node:fs");
const path = require("node:path");

const USER_AGENT =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36";

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function findPostPayload(profileDir) {
  const responses = readJson(path.join(profileDir, "network-responses.json"));
  const response = responses.find((item) => /\/aweme\/post\//.test(item.url));
  if (!response) {
    throw new Error(`No aweme post response in ${profileDir}`);
  }
  return JSON.parse(response.body);
}

function choosePlayUrl(item) {
  const candidates = [
    item.video?.play_addr_h264?.url_list,
    item.video?.play_addr?.url_list,
  ];
  for (const urls of candidates) {
    if (Array.isArray(urls) && urls.length > 0) return urls[0];
  }
  return null;
}

async function download(url, outputPath) {
  const response = await fetch(url, {
    redirect: "follow",
    headers: {
      "User-Agent": USER_AGENT,
      Referer: "https://www.douyin.com/",
    },
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText} for ${url}`);
  }
  const bytes = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(outputPath, bytes);
  return bytes.length;
}

async function main() {
  const [, , renderedRootArg, outputRootArg, countArg = "10"] = process.argv;
  if (!renderedRootArg || !outputRootArg) {
    console.error(
      "Usage: node download_douyin_samples.cjs <rendered-root> <output-root> [count]",
    );
    process.exit(2);
  }

  const renderedRoot = path.resolve(renderedRootArg);
  const outputRoot = path.resolve(outputRootArg);
  const sampleCount = Number.parseInt(countArg, 10);
  fs.mkdirSync(outputRoot, { recursive: true });

  const profileDirs = fs
    .readdirSync(renderedRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && /^creator-\d+$/.test(entry.name))
    .sort((left, right) => left.name.localeCompare(right.name));

  const manifest = {
    capturedAt: new Date().toISOString(),
    selectionRule: "Top public digg_count from the captured profile page, excluding zero-duration entries",
    profiles: [],
  };

  for (const profileEntry of profileDirs) {
    const profileDir = path.join(renderedRoot, profileEntry.name);
    const payload = findPostPayload(profileDir);
    const targetDir = path.join(outputRoot, profileEntry.name);
    fs.mkdirSync(targetDir, { recursive: true });

    const selected = payload.aweme_list
      .filter((item) => Number(item.duration) > 0 && choosePlayUrl(item))
      .sort(
        (left, right) =>
          Number(right.statistics?.digg_count || 0) -
          Number(left.statistics?.digg_count || 0),
      )
      .slice(0, sampleCount);

    const profileManifest = {
      label: profileEntry.name,
      hasMore: payload.has_more,
      maxCursor: payload.max_cursor,
      capturedCount: payload.aweme_list.length,
      samples: [],
    };

    for (let index = 0; index < selected.length; index += 1) {
      const item = selected[index];
      const rank = index + 1;
      const fileName = `${String(rank).padStart(2, "0")}-${item.aweme_id}.mp4`;
      const outputPath = path.join(targetDir, fileName);
      const playUrl = choosePlayUrl(item);
      const sizeBytes = await download(playUrl, outputPath);

      const sample = {
        rank,
        awemeId: item.aweme_id,
        description: item.desc,
        likes: Number(item.statistics?.digg_count || 0),
        durationMs: Number(item.duration || 0),
        width: Number(item.video?.width || 0),
        height: Number(item.video?.height || 0),
        localFile: path.relative(outputRoot, outputPath).replaceAll("\\", "/"),
        sizeBytes,
        sourceUrl: `https://www.douyin.com/video/${item.aweme_id}`,
      };
      profileManifest.samples.push(sample);
      console.log(JSON.stringify({ label: profileEntry.name, ...sample }));
    }

    manifest.profiles.push(profileManifest);
  }

  fs.writeFileSync(
    path.join(outputRoot, "sample-manifest.json"),
    JSON.stringify(manifest, null, 2),
    "utf8",
  );
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exit(1);
});
