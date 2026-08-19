#!/usr/bin/env python3
import argparse
import sys

verbose = False

def main(args):
    global verbose

    parser = argparse.ArgumentParser(
        description="set up dpp/InterviewQuestions/... based on the given problem number(s). e.g. 2.4 sets up dpp/InterviewQuestions/Chapter02-LinkedLists/2.4 with files and packages so that tests and algorithm code can be written in python there."
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("problems", nargs="*")
    parsed = parser.parse_args(args[1:])
    verbose = parsed.verbose

    for problem in parsed.problems:
        print(problem)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))