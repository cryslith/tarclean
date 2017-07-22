#!/usr/bin/python3


import argparse
import sys
import tarfile


def tarsort(infile, outstream):
   with tarfile.open(mode='r', fileobj=infile) as t_in:
       entries = sorted(t_in, key=lambda e: e.path)
       with tarfile.open(mode='w|', fileobj=outstream) as t_out:
           for entry in entries:
               t_out.addfile(entry,
                             fileobj=t_in.extractfile(entry)
                             if entry.isfile() else None)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('file')
    args = argparser.parse_args()
    if args.file == '-':
        raise ValueError("can't use stream")
    with open(args.file, 'rb') as infile:
        tarsort(infile, sys.stdout.buffer)
