#encoding:utf-8
import os
import time

from query_label_from_sha256 import get_label

from get_sha256 import get_sha256

from unzip import unzip_file

from load_zip import get_zip_list

from load_torrent import get_torrent_list

from update import judge_update

from load_url import get_html
from load_url import get_url_list

from core.setting import config
from core.setting import CONFIG_FILE
from core.setting import read_config

read_config(CONFIG_FILE)
print(555555555)
print(config) 


#get html
html = get_html(config.V_USERNAME,config.V_PASSWORD) 
#judge whether to update
content,url_path = judge_update(html,config.URL_DIR)
#get url
content = get_url_list(content,url_path)
#get .torrent file
torrent_paths = get_torrent_list(content,config.TORRENT_DIR)
#get .zip file
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



