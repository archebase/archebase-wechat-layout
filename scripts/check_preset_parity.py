#!/usr/bin/env python3
"""Assert canonical skill CSS equals InkPost preset payload."""

from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path


def extract_preset(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    match = re.search(r"css:\s*`([\s\S]*?)`\.trim\(\)", source)
    if not match:
        raise ValueError(f"could not find css template in {path}")
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inkpost_repo", type=Path)
    parser.add_argument("--css", type=Path, default=Path(__file__).parents[1] / "assets" / "archebase-wechat-safe.css")
    args = parser.parse_args()
    preset = args.inkpost_repo / "src/shared/presets/archebase-wechat-safe.ts"
    if not preset.is_file():
        parser.error(f"missing InkPost preset: {preset}")
    expected = args.css.read_text(encoding="utf-8").strip("\n")
    actual = extract_preset(preset).strip("\n")
    if expected != actual:
        print("FAIL: canonical CSS differs from InkPost preset payload")
        print("".join(difflib.unified_diff(expected.splitlines(True), actual.splitlines(True), fromfile=str(args.css), tofile=str(preset))))
        return 1
    print(f"OK: {preset} matches {args.css}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
