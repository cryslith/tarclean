# Reproducibility for tar files

Tar files come with metadata, which can be a problem for reproducible
builds.  These tools strip that metadata out.

# Usage

The following invocation should be sufficient to normalize most tar
files:

    tarsort input.tar | tarclean - >output.tar

# tarsort

`tarsort` sorts the entries in a tar file by path

# tarclean

`tarclean` removes the following metadata from each tar file entry:

* modification time
* UID
* GID
* username
* group name
* PAX headers

# Copyright

`tarclean` and `tarsort` are copyright 2017 Lily Chung <cryslith@protonmail.com>

`tarclean` and `tarsort` are available under the MIT license; see the
`LICENSE` file for more details.
