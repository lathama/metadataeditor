#!/usr/bin/env python
"""
Metadata Editor or Cleanup tool

For files in an input directory:
* Set the editor/creator metadata
* Set the title/description based on the filename.

Use cases:
* Correct titles of ripped DVDs
* Rename titles for DLNA client/server usage
* Version via editor/creator metadata

"""

import argparse
import glob
import os
import sys
sys.path.insert(0, 'mutagen-1.46.0-py3-none-any.whl')
import mutagen # pylint: disable=import-error,wrong-import-position

VERSION = 'Mediaeditor v1.0'
DEFAULT_TYPE = 'mp4'
DEFAULT_TOOL = 'MediaEditor V1.0'

def showmetadata(filename):
    """
    for a single file show the metadata found and print
    """
    print(mutagen.File(filename))

def showallmetadata(filepath):
    """
    for a single file show the metadata found and print
    """
    allfiles = filematchlist(filepath)
    for filename in allfiles:
        showmetadata(filename)

def filematchlist(filepath, filetype=DEFAULT_TYPE):
    """
    Return a list of files that match a type
    """
    filelist = glob.glob(filepath + '*.' + filetype )
    return filelist

def changemetadata(filename):
    """
    Edit the metadata of a file
    """
    print(filename + ' metadata before')
    showmetadata(filename)
    fileholder = mutagen.mp4.MP4(filename)
    fileholder['©nam'] = medianamecleanup(filename)
    fileholder['©too'] = DEFAULT_TOOL
    fileholder.save()
    print(filename + ' saved')
    print(filename + ' metadata after')
    showmetadata(filename)

def changeallmetadata(filepath):
    """
    Edit the metadata of all files in filepath
    """
    allfiles = filematchlist(filepath)
    for filename in allfiles:
        changemetadata(filename)

def medianamecleanup(filename):
    """
    Clean the path and extension along with underscores from filename
    """
    filepath = os.path.dirname(filename)
    cleanedname = filename.removeprefix(filepath + '/')
    cleanedname = cleanedname.replace('_', ' ')
    cleanedname = cleanedname.split('.')[0]
    return cleanedname

if __name__ == '__main__':
    theparser = argparse.ArgumentParser(
        prog='metadataeditor',
        description='Metadata Editor',
        epilog='by Andrew lathama Latham')
    groupa = theparser.add_mutually_exclusive_group(required=True)
    groupa.add_argument(
        '-s', '--show', action='store_true', help='Show Metadata')
    groupa.add_argument(
        '-c', '--change', action='store_true', help='Change Metadata')
    groupb = theparser.add_mutually_exclusive_group(required=True)
    groupb.add_argument(
        '-f', '--filename', help='Single Filename')
    groupb.add_argument(
        '-d', '--directory', help='Directory')
    theparser.add_argument(
        '-v', '--version', action='store_true', help='Show version')
    args = theparser.parse_args()
    if args.show:
        if args.filename:
            if os.path.isfile(args.filename):
                showmetadata(str(args.filename))
            else:
                print('File not found')
        if args.directory:
            if os.path.isdir(args.directory):
                showallmetadata(str(args.directory))
            else:
                print('Directory not found')
    if args.change:
        if args.filename:
            if os.path.isfile(args.filename):
                changemetadata(str(args.filename))
                #changemetadata('/media/media/media/Yellowstone_Bears.mp4')
            else:
                print('File not found')
        if args.directory:
            if os.path.isdir(args.directory):
                changeallmetadata(str(args.directory))
                #changeallmetadata('/media/media/media/')
            else:
                print('Directory not found')
