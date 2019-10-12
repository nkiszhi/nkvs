#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

FILE_TORRENTS = "./DATA/torrent.list"
DIR_DATA = "./DATA/"
list_torrents = []

paths = os.listdir(DIR_DATA)
for i in paths:
    #if i.find("VirusShare_0016") != -1:
    #    continue
    #if i.find("VirusShare_0017") != -1:
    #    continue
    #if i.find("VirusShare_0018") != -1:
    #    continue
    #if i.find("VirusShare_0019") != -1:
    #    continue
    if i.find(".added"):
        t = i.split('.added')[0] 
        print t
        print DIR_DATA+i
        print DIR_DATA+t
        shutil.move(DIR_DATA+i, DIR_DATA+t)
