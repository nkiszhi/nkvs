#encoding:utf-8
import os

from unzip import unzip_file

from load_file import get_file_list

from load_torrent import select
from load_torrent import get_torrent_list

from load_url import get_html
from load_url import get_url_list

from core.setting import config
from core.setting import CONFIG_FILE
from core.setting import read_config

read_config(CONFIG_FILE)
print(555555555)
print(config) 

html = get_html() 
new_content,appeared_content = get_url_list(html,config.URL_DIR)

content = select(new_content,appeared_content)
torrent_paths = get_torrent_list(content,config.TORRENT_DIR)

zip_dir = get_file_list(torrent_paths,config.ZIP_DIR)
print(zip_dir)
data_dir = unzip_file(zip_dir,config.DATA_DIR,config.PWD)

print("virusshare is in %s"%data_dir)
