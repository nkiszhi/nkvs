#encoding:utf-8
import os
import time

from unzip import unzip_file

from load_zip import get_zip_list

from load_torrent import get_torrent_list

from update import judge_upadte

from load_url import get_html
from load_url import get_url_list

from core.setting import config
from core.setting import CONFIG_FILE
from core.setting import read_config

read_config(CONFIG_FILE)
print(555555555)
print(config) 

second = 30*60
print(second)
#get html
html = get_html(config.V_USERNAME,config.V_PASSWORD) 
#judge whether to update
content = judge_update(html,config.URL_DIR)
#get url
content = get_url_list(content)
#get .torrent file
torrent_paths = get_torrent_list(content,config.TORRENT_DIR)
#get .zip file
zip_dir = get_zip_list(torrent_paths,config.ZIP_DIR)
print(zip_dir)
#get final file
while True:
    data_dir = unzip_file(zip_dir,config.DATA_DIR,config.U_PASSWORD)
    time.sleep(second)

print("virusshare is in %s"%data_dir)

