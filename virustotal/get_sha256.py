#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import hashlib
import pandas as pd

def get_sha256(data_dir):
    result = list()
    for dirpath,dirnames,filenames in os.walk(data_dir):
        for filename in filenames:
            if(len(filename)==64):
                result.append(filename)
            else:
                print(filename)
	        print(dirpath)
                file_path = os.path.join(dirpath,filename)
                print(dirnames)
                print(file_path)
                with open(file_path,'rb') as f:
                    sha256obj = hashlib.sha256()
                    sha256obj.update(f.read())
                    hash_value = sha256obj.hexdigest()
                    print(hash_value)
                    result.append(hash_value)
	            new_path = os.path.join(dirpath,hash_value)
	            os.rename(file_path,new_path)
        print(filenames)
    df = pd.DataFrame(result,columns=['sha256'])
    print(df)
    df.to_csv('./sample_table.csv')


