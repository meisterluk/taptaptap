#!/usr/bin/env python

"""Merge two TAP files"""

import sys
import tap
import argparse

def main(args):
    doc1 = tap.parse_file(args.file1)
    doc2 = tap.parse_file(args.file2)

    doc3 = doc1.merge(doc2)

    if args.outfile:
        with open(args.outfile, 'w') as fp:
            fp.write(doc3)
    else:
        print(doc3)

if __name__ == '__main__':
    # command line parameter parsing
    parser = argparse.ArgumentParser(description='Merge two TAP files.')
    parser.add_argument('file1', metavar='file1', help='The first TAP file')
    parser.add_argument('file2', metavar='file2', help='The second TAP file')
    parser.add_argument('-o', '--outputfile', dest='outfile', action='store',
                        help='write to filepath instead of stdout')

    main(parser.parse_args())
