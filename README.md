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
usage: metadataeditor [-h] (-s | -c | -v | -t) [-f FILENAME [FILENAME ...] | -d DIRECTORY] [-V]

Metadata Editor

options:
  -h, --help            show this help message and exit
  -s, --show            Show Metadata
  -c, --change          Change Metadata
  -v, --version         Show version
  -t, --runtests        Run Unit tests
  -f FILENAME [FILENAME ...], --filename FILENAME [FILENAME ...]
                        Filenames
  -d DIRECTORY, --directory DIRECTORY
                        Directory

  -V, --verbose         Show more output

by Andrew lathama Latham

$ ./metadataeditor.py -V -s -f waterfall.MP4
waterfall.MP4
        Name: ['waterfall']
        Artist: ['na']
        Comment: ['waterfall']
        Tool: ['Metadata Editor v1.1']
$ cp waterfall.MP4 Water_Fall.mp4
$ ./metadataeditor.py -V -s -f Water_Fall.mp4
Water_Fall.mp4
        Name: ['waterfall']
        Artist: ['na']
        Comment: ['waterfall']
        Tool: ['Metadata Editor v1.1']
$ ./metadataeditor.py -V -c -f Water_Fall.mp4
Change: metadata before
Water_Fall.mp4
        Name: ['waterfall']
        Artist: ['na']
        Comment: ['waterfall']
        Tool: ['Metadata Editor v1.1']
Change: metadata after
Water_Fall.mp4
        Name: ['Water Fall']
        Artist: ['na']
        Comment: ['Water Fall']
        Tool: ['Metadata Editor v1.1']
$
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


## Thanks

If you find this useful and want to say thanks I have an amazon wishlist

- https://www.amazon.com/hz/wishlist/ls/1L2X1DMW98TCQ
