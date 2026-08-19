#!/usr/bin/env python3
import argparse
import sys

verbose = False

def main(args):
    global verbose

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("filenames", nargs="*")
    parsed = parser.parse_args(args[1:])
    verbose = parsed.verbose

    for filename in parsed.filenames:
        print(filename)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))