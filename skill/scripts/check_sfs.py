#!/usr/bin/env python3
"""Check a Short Form Spec against the SFS rules.

Usage: python check_sfs.py <file.md>
Exit code 0 = pass (warnings allowed), 1 = fail.
"""
import re
import sys

MAX_WORDS = 500
REQUIRED = [
    "Summary",
    "Behavior",
    "Interfaces and data",
    "Key decisions",
    "Limitations and out of scope",
    "Verification",
    "References",
]
HISTORY = [
    r"\binitially\b", r"\boriginally\b", r"\bwe (first )?tried\b", r"\bpreviously\b",
    r"\breworked\b", r"\brefactored from\b", r"\bchanged from\b", r"\bused to\b",
    r"\bat first\b", r"\bearlier version\b", r"\binstead of the original\b",
]


def main(path):
    text = open(path, encoding="utf-8").read()
    # Count words outside fenced code blocks (code reads faster than prose).
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    words = len(re.findall(r"\S+", prose))
    errors, warnings = [], []

    if words > MAX_WORDS:
        errors.append(f"{words} words (prose, excluding code blocks); limit is {MAX_WORDS}.")

    headings = {h.strip().lower() for h in re.findall(r"^##\s+(.+)$", text, flags=re.M)}
    for section in REQUIRED:
        if section.lower() not in headings:
            errors.append(f"Missing section: {section}")

    for pattern in HISTORY:
        for m in re.finditer(pattern, text, flags=re.I):
            line = text.count("\n", 0, m.start()) + 1
            warnings.append(f"Possible rework/history language on line {line}: '{m.group(0)}'")

    if re.search(r"<[^>\n]+>", text):
        warnings.append("Unfilled <placeholder> text remains.")

    print(f"{path}: {words} words")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    if not errors and not warnings:
        print("OK")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))