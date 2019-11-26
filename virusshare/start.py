#encoding:utf-8
import os
import time
import argparse
from core.setting import read_config
from core.setting import CONFIG_FILE
from core.setting import config

from get_vslist import get_url_list
from get_vslist import get_html
from check_update import judge_update
from get_torrents import get_torrent_list
from get_zip import get_zip_list
from unzip_samples import unzip_file
from get_sha256 import get_sha256
from mov_sha256 import move_file


parser = argparse.ArgumentParser(usage="python start.py -u <username> -p <password> ",description="help info")
parser.add_argument("-u","--username",type = str,required = True,help = "the username for login",dest="usr")
parser.add_argument("-p","--password",type = str,required = True,help = "the password for login",dest="pwd")
args = parser.parse_args()

    
read_config(CONFIG_FILE)
#print(555555555)
print(config) 


#get html
html = get_html(args.usr,args.pwd) 
#judge whether to update
content,url_path = judge_update(html,config.URL_DIR)
#get url
content = get_url_list(content,url_path)
#get torrent file
torrent_paths = get_torrent_list(content,config.TORRENT_DIR)
#get zip file
zip_dir = get_zip_list(torrent_paths,config.ZIP_DIR)
print(zip_dir)
#get file
data_dir = unzip_file(zip_dir,config.DATA_DIR,config.U_PASSWORD)
print("virusshare is in %s"%data_dir)
#get sha256 and rename
get_sha256(data_dir)
#move file
move_file(data_dir,config.SHA256_DIR)
#get label
get_label()



