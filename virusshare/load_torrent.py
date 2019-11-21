#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests 
import re
import os

def get_torrent_list(content,torrent_dir):
    torrent_paths = []
    print(111111111)
    if(torrent_dir):
        if not os.path.exists(torrent_dir):
            os.mkdir(torrent_dir)
        for raw_url in content:
            url = raw_url.strip()
            torrent_path = os.path.join(torrent_dir,url.split('?')[0].split('/')[-1])
            print(url)
            print(torrent_path)
            torrent_paths.append(torrent_path)
            r = requests.get(url,verify=False)
            print(22222222)
            with open(torrent_path,'wb') as f:
                f.write(r.content)
                print("file saved")
    else:
        exit("[!]no '%s'"% torrent_dir)
    return torrent_paths
    
    
