import pandas as pd
import os

def move_file(data_dir,sha256_dir):
    if(sha256_dir):
        if not os.path.exists(sha256_dir):
            os.mkdir(sha256_dir)
    	for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath,filename)
                sha256_path = os.path.join(sha256_dir,filename[0],filename[1],filename[2],filename[3])
                print(sha256_path)
                if not os.path.exists(sha256_path):
                    os.makedirs(sha256_path)
	        dst = 'mv '+file_path+' '+sha256_path
	        os.popen(dst)        
    else:
        exit("[!]no '%s'"%sha256_dir)	
    

