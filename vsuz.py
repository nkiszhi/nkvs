#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# folder for virusshare samples
DIR_DATA = "/home/RaidDisk/"
# folder for virusshare zip files
DIR_ZIP = "/home/RaidDisk/virusshare/"
# password for zip files
PASSWORD = "infected"

def extract():
    z = os.listdir(DIR_ZIP)
    for f in z:
        print DIR_ZIP+f
        os.popen("unzip -o -P " + PASSWORD + " " + DIR_ZIP+f + " -d " + DIR_DATA)
    pass

def get_sha256():
    pass

def main():
    extract()

main()
