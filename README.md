# Metadata Editor

by Andrew "lathama" Latham

## Background

I needed to cleanup the metadata name on a large number of MP4 files.

* Ripping DVDs with makeMKV and processing with Handbrake
* Serving over DLNA via minidlna
* Devices displayed incorrect or hard to understand names
* One DVD that was a double feature had both titles for each feature

## Usage

```
$ ./metadataeditor.py -h
usage: metadataeditor [-h] (-s | -c) (-f FILENAME | -d DIRECTORY) [-v]

Metadata Editor

optional arguments:
  -h, --help            show this help message and exit
  -s, --show            Show Metadata
  -c, --change          Change Metadata
  -f FILENAME, --filename FILENAME
                        Single Filename
  -d DIRECTORY, --directory DIRECTORY
                        Directory
  -v, --version         Show version

by Andrew lathama Latham
```

## Requirements

I found mutagen[1] as an easy tool to use for this. I am doing a local whl import to keep this portable.

## Quality

```
$ pylint metadataeditor.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## TODO

* Check file types and more general input checking
* support more than just MP4

## Resources

1. https://github.com/quodlibet/mutagen

