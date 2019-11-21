#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import re
import os

def judge_update(html,url_dir):
    if(html):
        if(url_dir):
            if not os.path.exists(url_dir):
                os.mkdir(url_dir)
            url_path = os.path.join(url_dir,"url_list.txt")
            new_content = re.findall(r"<a.*?href=\"(.*VirusShare_.*)\">.*<\/a>",html,re.I)
            if not os.path.exists(url_path):
                print("this is first come")
                return new_content,url_path
            else:
                f = open(url_path,'r')
                old_content = list(f)
                for i in range(len(old_content)):
                    old_content[i]=old_content[i].strip('\n')
                old_content = set(old_content)
                print(old_content)
                print(2333333)
                new_content = set(new_content)
                print(new_content)
                appeared_content = new_content - old_content
                if not appeared_content:
                     exit("[!]no update")
                else:
                     print("something update")
                     return appeared_content,url_path
        else:           
            exit("[!]no '%s'"% url_dir)
    else:
        exit("[!]missing website")
