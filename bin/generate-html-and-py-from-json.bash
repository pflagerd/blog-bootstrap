#!/bin/bash
# Run the script from the working directory containing problem.json
#
mydirname="$(realpath $(dirname "${BASH_SOURCE[0]}"))" >/dev/null
echo $mydirname
