#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os
import zipfile

# folder for virusshare samples
DIR_DATA = "/home/RaidDisk/"
# folder for virusshare zip files
DIR_ZIP = "/home/RaidDisk/virusshare/"
# password for zip files
PASSWORD = "infected"

# use sample sha256 number as foler names. The first level uses the first
# number in the sha256 value, and so on. In total there are 4 levels. 
def init_dir():
    for i in range(16):
        for j in range(16):
            for k in range(16):
                for l in range(16):
                    os.popen("mkdir -p " + DIR_DATA + hex(i)[2] + "/" +
                            hex(j)[2] + "/" + hex(k)[2] + "/"+hex(l)[2])
                    print DIR_DATA + hex(i)[2] + "/" + hex(j)[2] + "/" + hex(k)[2] + "/"+hex(l)[2]
                    os.popen("touch " + DIR_DATA + hex(i)[2] + "/" + hex(j)[2]
                            + "/" + hex(k)[2] + "/"+hex(l)[2] + "reports.csv")
    pass


def main():
    init_dir()

main()



