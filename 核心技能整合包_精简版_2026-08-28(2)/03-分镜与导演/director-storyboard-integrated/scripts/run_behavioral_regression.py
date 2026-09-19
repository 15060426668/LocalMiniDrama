#!/usr/bin/env python3
"""Run registered behavioral storyboard/SD regression artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from validate_storyboard_sd import DEFAULT_CONTRACT, validate_sd, validate_source_mapping, validate_storyboard


DEFAULT_CASES = Path(__file__).with_name("behavioral-regression-cases.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--allow-pending", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    registry = json.loads(args.cases.read_text(encoding="utf-8"))
    contract = json.loads(DEFAULT_CONTRACT.read_text(encoding="utf-8"))
    results = []

    for case in registry["cases"]:
        path = args.output_directory / f"{case['id']}.md"
        if not path.exists():
            results.append({"id": case["id"], "status": "pending", "path": str(path)})
            continue
        text = path.read_text(encoding="utf-8")
        findings = validate_storyboard(text, contract, False)
        if "【A区块" in text:
            findings.extend(validate_sd(text, contract, strict_complexity=True))
            findings.extend(validate_source_mapping(text, text, contract, strict_source_coverage=True))
        missing_groups = [
            group for group in case["required_term_groups"] if not any(term in text for term in group)
        ]
        forbidden_groups = [
            group
            for group in case.get("forbidden_term_groups", [])
            if any(term in text for term in group)
        ]
        errors = [finding.message for finding in findings if finding.level == "ERROR"]
        warnings = [finding.message for finding in findings if finding.level == "WARNING"]
        status = "pass" if not errors and not missing_groups and not forbidden_groups else "fail"
        results.append(
            {
                "id": case["id"],
                "status": status,
                "path": str(path),
                "missing_term_groups": missing_groups,
                "forbidden_term_groups": forbidden_groups,
                "errors": errors,
                "warnings": warnings,
            }
        )

    summary = {
        "suite_version": registry["suite_version"],
        "pass": sum(item["status"] == "pass" for item in results),
        "fail": sum(item["status"] == "fail" for item in results),
        "pending": sum(item["status"] == "pending" for item in results),
        "results": results,
    }
    if args.as_json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"pass={summary['pass']} fail={summary['fail']} pending={summary['pending']}")
        for item in results:
            print(f"{item['id']}: {item['status']}")

    if summary["fail"]:
        return 1
    if summary["pending"] and not args.allow_pending:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
