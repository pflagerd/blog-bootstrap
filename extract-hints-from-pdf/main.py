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


def format_text_as_json(text: str) -> str:
    """
    Extract:
      - labels like #1. .. #12.
      - section refs like 1.2, 3.1, ...
      - hint paragraphs

    Ignore everything in the PDF before the first '#1.' line.
    """

    #text = normalize_whitespace(text)

    # ---- NEW STEP: discard everything before '#1.' ----
    start = re.search(r'(?m)^#1\.', text)
    if not start:
        raise ValueError("Could not find '#1.' in extracted text.")

    text = text[start.start():]
    # ---------------------------------------------------

    text = re.split(r'(?=#\d+\.)', text)[1:]

    things = [ re.sub(r"\n +", " ", t.strip()).replace('\u00ad', '') for t in text ]
    things = [ re.sub(r'"', "\\\"", t) for t in things ]

    # Remove headers and footers.
    # Greedily remove text containing Hints for Data Structures preceded by one or more newlines and non-newline characters (Should leave the hint text itself alone)
    things = [ re.sub(r'\n+.+Hints for.*', "", thing, flags=re.DOTALL) for thing in things ]
    things = [ re.sub(r'\n+.+CrackingThe.*$', "", thing, flags=re.DOTALL | re.MULTILINE) for thing in things ]

    json = ""
    for thing in things:
        triple = re.split(r'  +', thing)
        if triple[0] == "#255.":
            print([(c, ord(c)) for c in triple[2]])
        json += '{ "' + triple[0] + '": "' + triple[2].strip() + '" }\n'

    return json


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} input.pdf", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(sys.argv[1])

    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        json_formatted_text = format_text_as_json(extracted_text)
        json_output_path = pdf_path.with_suffix(".extracted.json")
        json_output_path.write_text(json_formatted_text, encoding="utf-8")
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    print("wrote ",len(json_formatted_text.split('\n')), " lines to ", json_output_path)


if __name__ == "__main__":
    main()