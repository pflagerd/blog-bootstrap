# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This directory is a `blog-bootstrap`-derived repo (`origin` = `git@github.com:pflagerd/blog-bootstrap.git`, current branch `cracking-the-coding-interview`) that has been *branched* into the larger `algorithms` monorepo as a subdirectory: `algorithms/doc/Cracking the Coding Interview`. Two things live here side by side:

1. A **collapsible-article blog** (`index.html`, `meta-blog.html`, `blog.css`, `blog.js`) — the standard blog-bootstrap mechanism, described further below.
2. A **problem-set workspace** for working through *Cracking the Coding Interview* (`djf/` and `dpp/` — two independent people's solutions, one per chapter/problem).

Because this repo is branched (not forked) from blog-bootstrap, `blog.css`/`blog.js` fixes here are local to this branch — see `README.md` for the fork-vs-branch distinction before assuming changes should propagate elsewhere.

## Problem-set workspace (`djf/`, `dpp/`)

Each person's solutions live under `<person>/InterviewQuestions/Chapter<NN>-<Name>/<problem-number>/`. Note the two directories use **different chapter-naming conventions**: `dpp` zero-pads (`Chapter02-LinkedLists`), `djf` does not (`Chapter1-ArraysAndStrings`). Don't assume one pattern works for both.

A problem directory follows a generated scaffold, self-documented by its own `.dirinfo` file:

- `problem.json` — source of truth: title, PDF `url` anchor, `statement`, `hints` (keyed by hint number, e.g. `"#72"`, matching `extract-hints-from-pdf/ctci_hints.json`), `constraints-and-assumptions`, `timeComplexity`, `spaceComplexity`, `examples`, `tests`.
- `problem.html` — generated from `problem.json` (do not hand-edit; regenerate instead).
- `problem.py` — generated stub + `unittest` test cases (also derived from `problem.json`, then hand-edited to add the real solution).
- `RUNME` — runs `python -m unittest ./problem.py` from that directory.
- `SETMEUP` — sourced by `RUNME`; checks/sets up the environment (per-problem `.venv`, etc.).
- `problem-solving-procedure.html` (where present) — a per-problem checklist/log of the solving process; `problem-solving-procedure-prototype.html` at the repo root is the template/prototype for this.

### Running a single problem's tests

```bash
cd dpp/InterviewQuestions/Chapter02-LinkedLists/2.3   # or any problem directory
./RUNME
```
This is equivalent to `python -m unittest ./problem.py` run from inside that directory (paths in `problem.py`/tests are relative to cwd).

### Regenerating `problem.html` / `problem.py` from `problem.json`

```bash
cd <problem-directory>          # must contain problem.json
"../../../../bin/generate-html-and-py-from-json.bash"   # adjust ../ depth to reach repo root's bin/
```
This script (`bin/generate-html-and-py-from-json.bash`) must be run **from the directory containing `problem.json`**. It shells out to generator scripts that live *outside* this repo, in the sibling `algorithms/practice/python/generate-problem-html-from-problem-json/` and `.../generate-problem-py-from-problem-json/` directories (each with its own `RUNME`/`SETMEUP` that provisions a local `.venv` with Jinja2). If those generator scripts are missing or fail, this repo alone won't have them — they belong to the parent `algorithms` checkout.

**Known drift:** `generate-problem-py-from-problem-json.py`'s schema expectations (flat `test.expectedResult` fields) don't match the current `problem.json` `tests` shape used in this repo (`"expected output": {"type": ..., "value": ...}` plus an `"input"` list of typed args). Verify generated `problem.py` output before trusting it wholesale.

### Hints pipeline

`extract-hints-from-pdf/extract-hints-0.py` pulls the numbered hints appendix out of the CTCI PDF (via the external `pdftotext`/poppler-utils command) into `extract-hints-from-pdf/ctci_hints.json`, keyed by hint number and containing `[problem-number, hint-text]`. `problem.json`'s `hints` map (e.g. `"#72": "..."`) is meant to be cross-referenced against this file.

### Chapter scaffolding

`create-chapter-directories/main.py` creates the 15 `Chapter<N>-<Name>` directories for a fresh person's `InterviewQuestions/` tree (run from inside that person's `InterviewQuestions/` directory).

## Blog mechanism (`index.html`, `meta-blog.html`, `blog.css`, `blog.js`)

- `index.html` is this project's blog (progress journal, problem write-ups); `meta-blog.html` is the blog-bootstrap dev-log — entries about the blog mechanism's own implementation/fixes.
- Both are static, chromium-centric, file-only pages (`file://`, no server) styled by `blog.css` and behavior-driven by `blog.js`.
- `blog.js` finds every `<article>`, injects an Expand/Collapse toggle into its first child, and animates height between a "collapsed preview" (the heading plus any immediately-following `.meta` siblings) and full height. Collapse state persists per-article in `localStorage`, keyed by the article's `id`. When editing this file, note the comments explaining why height is measured via `getBoundingClientRect()` rather than summed from individual child heights (inline-wrapping siblings of different heights break naive summation).
- `inline-index-html.mjs` inlines an `index.html`/`meta-blog.html` into a standalone file: `node inline-index-html.mjs input.html output.html`.
- `problem-solving-procedure-prototype.html` is a separate, self-contained styled prototype (its own inline CSS, not `blog.css`) for a per-problem procedure checklist — treat CSS/markup changes there as isolated from the blog.css/blog.js system unless told otherwise.

## Other utilities

- `display-text-file/` — a small standalone Express app (`npm start`, runs `server.js`) that serves a text file with line numbers in the browser. Independent `package.json`; not wired into the rest of the repo.

## Working notes

- Generated files (`problem.html`, `problem.py` prior to hand-edits) should be treated as regenerable outputs of `problem.json`, not primary sources — prefer editing `problem.json` and regenerating over hand-patching generated HTML.
- `.venv/`, `__pycache__/`, and `.idea/` directories appear throughout `djf/`/`dpp/` problem directories; these are local tooling artifacts, not something to inspect for problem content.
