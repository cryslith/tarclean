#!/usr/bin/python3


import argparse
import sys
import tarfile


NEW_MTIME = 0


def tarclean(instream, outstream):
   with tarfile.open(mode='r|', fileobj=instream) as t_in:
       with tarfile.open(mode='w|', fileobj=outstream) as t_out:
           for entry in t_in:
               entry.mtime = NEW_MTIME
               entry.uid = 0
               entry.gid = 0
               entry.uname = ''
               entry.gname = ''
               entry.pax_headers = {}
               t_out.addfile(entry,
                             fileobj=t_in.extractfile(entry)
                             if entry.isfile() else None)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('file')
    args = argparser.parse_args()
    if args.file == '-':
        tarclean(sys.stdin.buffer, sys.stdout.buffer)
    else:
        with open(args.file, 'rb') as infile:
            tarclean(infile, sys.stdout.buffer)
