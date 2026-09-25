#!/usr/bin/env python3
"""Validate the canonical ArcheBase InkPost WeChat CSS contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

APPROVED_COLORS = {
    "0032ff", "7172fa", "619afd", "46cfff", "1e2124",
    "ffffff", "f2f5ff", "f3f5ff", "f4f7ff", "f7f8ff",
    "bfc8ff", "e9edff",
}
FORBIDDEN_PROPERTIES = {
    "animation", "backdrop-filter", "clip-path", "columns", "filter",
    "mask", "object-fit", "position", "transform", "transition", "writing-mode",
}
FORBIDDEN_DISPLAYS = {"flex", "grid", "inline-flex", "inline-grid"}
HEX_COLOR = re.compile(r"#([0-9a-f]{3}|[0-9a-f]{6})(?![0-9a-f])", re.I)
DECLARATION = re.compile(r"(?m)^\s*([\w-]+)\s*:\s*([^;{}]+)")


def compact_hex(value: str) -> str:
    value = value.lower()
    return "".join(char * 2 for char in value) if len(value) == 3 else value


def validate(css: str) -> list[str]:
    errors: list[str] = []
    for match in DECLARATION.finditer(css):
        prop, value = match.groups()
        prop = prop.lower()
        value = value.strip().lower()
        line = css.count("\n", 0, match.start()) + 1
        if prop in FORBIDDEN_PROPERTIES:
            errors.append(f"line {line}: WeChat-unsafe property `{prop}`")
        if prop == "display" and any(display in value for display in FORBIDDEN_DISPLAYS):
            errors.append(f"line {line}: WeChat-unsafe display `{value}`")
        if re.search(r"\borange\b|#ff(?:[0-9a-f]{4}|[0-9a-f]{2})\b", value, re.I) and "#ffffff" not in value:
            errors.append(f"line {line}: orange-like value `{value}` is not an approved ArcheBase article CTA/status color")
    if re.search(r"\blinear-gradient\s*\(", css, re.I):
        errors.append("gradient dependency: ordinary InkPost article layout must not rely on linear-gradient")
    for match in HEX_COLOR.finditer(css):
        color = compact_hex(match.group(1))
        if color not in APPROVED_COLORS:
            line = css.count("\n", 0, match.start()) + 1
            errors.append(f"line {line}: color `#{match.group(1)}` is outside the approved InkPost article palette")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("css", type=Path)
    args = parser.parse_args()
    if not args.css.is_file():
        parser.error(f"CSS file does not exist: {args.css}")
    errors = validate(args.css.read_text(encoding="utf-8"))
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"OK: {args.css}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
