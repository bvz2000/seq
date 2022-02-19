#! /usr/bin/env python3

import os
import sys

from bvzframespec import Framespec

files = os.listdir(sys.argv[1])

fs = Framespec()
file_groups = fs.separate_list_into_lists_of_similar(files)
for file_group in file_groups:
    fs.files_list = file_group
    if "-m" in sys.argv:
        print(fs.condensed_files_str, "missing:", fs.missing)
    else:
        print(fs.condensed_files_str)
