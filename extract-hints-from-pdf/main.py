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
    from a text dump similar to the sample you pasted.
    """
    lines = [line.strip() for line in normalize_whitespace(text).splitlines()]
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

    # Remove standalone noise/header lines if present
    # Adjust this set as needed for your source PDF.
    noise = {
        "I",
        "Hints for Data Structures",
    }
    remainder = [line for line in remainder if line not in noise]

    # Reconstruct paragraphs:
    # lines that belong to the same paragraph are joined until we heuristically
    # detect the next sentence-group beginning with an uppercase letter and the
    # current one seems complete enough.
    #
    # For your sample, a simpler rule works well:
    # each logical hint is already in sequence, so we accumulate until the
    # current text looks sentence-complete and long enough.
    hints: list[str] = []
    current: list[str] = []

    for line in remainder:
        current.append(line)

        joined = " ".join(current)

        # Heuristic: if we end in punctuation and have a reasonable amount of text,
        # treat it as one hint.
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