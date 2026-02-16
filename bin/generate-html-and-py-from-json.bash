#!/bin/bash
# Run the script from the working directory containing problem.json
#
mydirname="$(realpath "$(dirname "${BASH_SOURCE[0]}")")" >/dev/null
"$mydirname/../../../practice/python/generate-problem-html-from-problem-json/"RUNME
"$mydirname/../../../practice/python/generate-problem-py-from-problem-json/"RUNME ./problem.json