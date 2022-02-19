#! /usr/bin/env python3

import os
import sys

from bvzframespec import Framespec

if "-m" in sys.argv:
    missing = True
    sys.argv.remove("-m")
else:
    missing = False

if "-h" in sys.argv:
    hidden = True
    sys.argv.remove("-h")
else:
    hidden = False

if "-d" in sys.argv:
    dirs = True
    sys.argv.remove("-d")
else:
    dirs = False

if len(sys.argv) > 2 or "-u" in sys.argv or "--help" in sys.argv or "--usage" in sys.argv:
    print(f"Usage: {sys.argv[0]} <directory> <-m> <-h> <-d>")
    print()
    print("directory is optional. If omitted, the current working directory will be used.")
    print("-m will show missing files from a sequence. Optional.")
    print("-h will include hidden files. Optional.")
    print("-d will include directories. Optional.")
    sys.exit()

if len(sys.argv) == 1:
    directory = os.getcwd()
else:
    directory = sys.argv[1]

files = os.listdir(directory)

fs = Framespec()
file_groups = fs.separate_list_into_lists_of_similar(files)
for file_group in file_groups:
    if not hidden and file_group[0].startswith("."):
        continue
    if not dirs and os.path.isdir(os.path.join(directory, file_group[0])):
        continue
    fs.files_list = file_group
    if missing:
        print(fs.condensed_files_str, "missing:", fs.missing)
    else:
        print(fs.condensed_files_str)
