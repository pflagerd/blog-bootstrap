#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract text from a PDF using the external `pdftotext` command.

    Requires:
        pdftotext (from poppler-utils) to be installed and on PATH.
    """
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if shutil.which("pdftotext") is None:
        raise RuntimeError(
            "pdftotext is not installed or not on PATH.\n"
            "On Debian/Ubuntu/Kubuntu: sudo apt install poppler-utils"
        )

    # Write output to stdout by using '-' as the text-file argument.
    # -layout often preserves line/group structure better for this kind of extraction.
    cmd = [
        "pdftotext",
        "-layout",
        "-nopgbrk",
        str(pdf_path),
        "-",
    ]

    result = subprocess.run(
        cmd,
        check=True,
        text=True,
        capture_output=True,
    )

    return result.stdout


def normalize_whitespace(text: str) -> str:
    # Normalize line endings and trim trailing spaces
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    return text


def parse_rearrangeable_blocks(text: str) -> tuple[list[str], list[str], list[str]]:
    """
    Extract:
      - labels like #1. .. #12.
      - section refs like 1.2, 3.1, ...
      - hint paragraphs

    Ignore everything in the PDF before the first '#1.' line.
    """

    text = normalize_whitespace(text)

    # ---- NEW STEP: discard everything before '#1.' ----
    start = re.search(r'(?m)^#1\.', text)
    if not start:
        raise ValueError("Could not find '#1.' in extracted text.")

    text = text[start.start():]
    # ---------------------------------------------------

    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    label_pattern = re.compile(r"^#\d+\.$")
    section_pattern = re.compile(r"^\d+\.\d+$")

    labels: list[str] = []
    sections: list[str] = []
    remainder: list[str] = []

    for line in lines:
        if label_pattern.fullmatch(line):
            labels.append(line)
        elif section_pattern.fullmatch(line):
            sections.append(line)
        else:
            remainder.append(line)

    # remove common header noise
    noise = {
        "I",
        "Hints for Data Structures",
    }
    remainder = [line for line in remainder if line not in noise]

    # reconstruct hint paragraphs
    hints: list[str] = []
    current: list[str] = []

    for line in remainder:
        current.append(line)
        joined = " ".join(current)

        if re.search(r'[.?!]["\']?$', joined) and len(joined) > 60:
            hints.append(joined)
            current = []

    if current:
        hints.append(" ".join(current))

    return labels, sections, hints


def rearrange_text(text: str) -> str:
    labels, sections, hints = parse_rearrangeable_blocks(text)

    if not (len(labels) == len(sections) == len(hints)):
        raise ValueError(
            "Could not align extracted data cleanly.\n"
            f"Found {len(labels)} labels, {len(sections)} section refs, "
            f"and {len(hints)} hint paragraphs.\n"
            "You may need to tweak the parsing rules for your particular PDF."
        )

    width = max(len(label) for label in labels)
    lines = [
        f"{label:<{width}}    {section:<6}  {hint}"
        for label, section, hint in zip(labels, sections, hints)
    ]
    return "\n\n".join(lines)


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} input.pdf", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(sys.argv[1])

    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        rearranged = rearrange_text(extracted_text)
        raw_txt_path = pdf_path.with_suffix(".extracted.txt")
        raw_txt_path.write_text(extracted_text, encoding="utf-8")
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    print(rearranged)


if __name__ == "__main__":
    main()