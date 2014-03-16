#!/usr/bin/env python

"""
Reads a TAP file and exit status indicates success:
  0:  everything is fine
  1:  some testcase is missing or failed
  2:  A bailout was thrown
If some text occurs at stderr, taptaptap has a problem
"""

import sys
import taptaptap
import argparse

def main(args):
    doc = taptaptap.parse_file(args.report)
    if doc.bailed():
        return 2
    elif doc.valid():
        return 0
    else:
        return 1

if __name__ == '__main__':
    # command line parameter parsing
    desc = 'Does the TAP file indicate an error?'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('report', metavar='report', help='the TAP file to read')

    sys.exit(main(parser.parse_args()))
