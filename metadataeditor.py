#!/usr/bin/env python
"""
Metadata Editor
by Andrew lathama Latham

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
import unittest
sys.path.insert(0, 'mutagen-1.47.0-py3-none-any.whl')
import mutagen # pylint: disable=import-error,wrong-import-position

DEFAULT_TYPE = 'mp4'
DEFAULT_TOOL = 'Metadata Editor v1.1'
VERBOSE = False
VERSION = 'Metadata Editor v1.1'

def showmetadata(filename):
    """
    for a single file show the metadata found and print
    """
    print(filename)
    fileinfo = mutagen.File(filename)
    if '©nam' in fileinfo:
        print('\tName: ' + str(fileinfo['©nam']))
    if VERBOSE:
        if '©ART' in fileinfo:
            print('\tArtist: ' + str(fileinfo['©ART']))
        if '©cmt' in fileinfo:
            print('\tComment: ' + str(fileinfo['©cmt']))
        if '©too' in fileinfo:
            print('\tTool: ' + str(fileinfo['©too']))

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
    print('Change: metadata before')
    showmetadata(filename)
    fileholder = mutagen.mp4.MP4(filename)
    fileholder['©ART'] = "na"
    fileholder['©cmt'] = medianamecleanup(filename)
    fileholder['©nam'] = medianamecleanup(filename)
    fileholder['©too'] = DEFAULT_TOOL
    fileholder.save()
    print('Change: metadata after')
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

class Testmetadataeditor(unittest.TestCase):
    """
    Unit testing just a few functions because reasons
    """
    def setUp(self):
        """
        Setup some useful variables
        """
        self.filename_good = 'my_movie.mp4'
        self.filename_bad = 'my.movie.mp4_.mp4'
        self.filename_result_good = 'my movie'

    def test_medianamecleanup(self):
        """
        Test the filenames are as expected
        """
        self.assertEqual(
            medianamecleanup(self.filename_good), self.filename_result_good)
        self.assertNotEqual(
            medianamecleanup(self.filename_bad), self.filename_result_good)

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
    groupa.add_argument(
        '-v', '--version', action='store_true', help='Show version')
    groupa.add_argument(
        '-t', '--runtests', action='store_true', help='Run Unit tests')
    groupb = theparser.add_mutually_exclusive_group()
    groupb.add_argument(
        '-f', '--filename', help='Filenames', nargs='+')
    groupb.add_argument(
        '-d', '--directory', help='Directory')
    groupc = theparser.add_argument_group()
    groupc.add_argument(
        '-V', '--verbose', action='store_true', help='Show more output')
    args = theparser.parse_args()
    if args.verbose:
        VERBOSE = True
    if args.show:
        if args.filename:
            for entry in args.filename:
                if os.path.isfile(entry):
                    showmetadata(str(entry))
                else:
                    print('File not found')
        if args.directory:
            if os.path.isdir(args.directory):
                showallmetadata(str(args.directory))
            else:
                print('Directory not found')
    if args.change:
        if args.filename:
            for entry in args.filename:
                if os.path.isfile(entry):
                    changemetadata(str(entry))
                else:
                    print('File not found')
        if args.directory:
            if os.path.isdir(args.directory):
                changeallmetadata(str(args.directory))
                #changeallmetadata('/media/media/media/')
            else:
                print('Directory not found')
    if args.version:
        print(VERSION)
    if args.runtests:
        del sys.argv[1:]
        unittest.main(verbosity=2)
