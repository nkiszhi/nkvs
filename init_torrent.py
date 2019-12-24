#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Remove the ".added" suffix of torrent files at
DATA folder """

import shutil

DIR_DATA = "./DATA/"
list_torrents = []

paths = os.listdir(DIR_DATA)
for i in paths:
    if i.find(".added"):
        t = i.split('.added')[0] 
        print t
        src_file = DIR_DATA+i
        dst_file = DIR_DATA+t
        shutil.move(src_file, dst_file)
