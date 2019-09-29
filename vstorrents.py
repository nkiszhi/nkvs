#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

FILE_TORRENTS = "./DATA/torrent.list"
DIR_DATA = "./"
list_torrents = []

paths = os.listdir(DIR_DATA)
for i in paths:
  print i

  t = i.split('?')[0] 
  print t
  shutil.move(DIR_DATA+i, DIR_DATA+t)
