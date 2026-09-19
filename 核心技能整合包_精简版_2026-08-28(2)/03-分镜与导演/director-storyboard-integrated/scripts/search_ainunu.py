#!/usr/bin/env python3
"""Search the Ainunu film/TV catalog using its GBK query encoding."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote_from_bytes, urljoin
from urllib.request import Request, urlopen


BASE_URL = "https://video.ainunu.com"
SEARCH_URL = f"{BASE_URL}/plus/search.php"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138 Safari/537.36"


def fetch(url: str, timeout: int) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        payload = response.read()
    return payload.decode("gbk", errors="replace")


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def search(query: str, limit: int, timeout: int, resolve: bool) -> dict:
    encoded = quote_from_bytes(query.encode("gbk", errors="replace"))
    url = f"{SEARCH_URL}?kwtype=0&titlekeyword=1&keyword={encoded}"
    page = fetch(url, timeout)
    matches = re.findall(
        r'<a\s+href=["\'](?P<href>/c/(?:movie|dsj)/[^"\']+\.html)["\'][^>]*>(?P<title>.*?)</a>',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )

    results = []
    seen = set()
    for href, title_html in matches:
        detail_url = urljoin(BASE_URL, href)
        if detail_url in seen:
            continue
        seen.add(detail_url)
        item = {"title": clean_text(title_html), "detail_url": detail_url}
        if resolve:
            try:
                detail_page = fetch(detail_url, timeout)
                resource = re.search(
                    r'<a[^>]+id=["\']ziyuan["\'][^>]+href=["\']([^"\']+)["\']',
                    detail_page,
                    flags=re.IGNORECASE,
                )
                item["resource_url"] = html.unescape(resource.group(1)) if resource else None
            except (HTTPError, URLError, TimeoutError) as exc:
                item["resource_error"] = str(exc)
        results.append(item)
        if len(results) >= limit:
            break

    return {
        "query": query,
        "search_url": url,
        "encoding": "GBK",
        "result_count": len(results),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Chinese or English film/TV title")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--resolve", action="store_true", help="Resolve public resource-page links from detail pages")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()

    try:
        result = search(args.query, max(1, args.limit), max(1, args.timeout), args.resolve)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(json.dumps({"query": args.query, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
