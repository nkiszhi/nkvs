#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import zipfile

def unzip_file(zip_dir,data_dir,password):
    if(data_dir):
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        for file_name in os.listdir(zip_dir):
            zip_name = os.path.join(zip_dir,file_name) 
            file_name = file_name.split('.')[0]
            print(file_name)
            dst_dir = os.path.join(data_dir,file_name) 
            print(dst_dir)
            r = zipfile.is_zipfile(zip_name)
            if r:
                zf = zipfile.ZipFile(zip_name,'r')
                #print(56789)
                zf.extractall(path=dst_dir,pwd=password)
                #print(12345)
            else:
                print("This is not zip")
    else:
        exit("[!]no '%s'"% data_dir)
    return os.path.abspath(data_dir)

if __name__ == '__main__':
    root = unzip_file('./zip','./data','infected')
    print(11111)
