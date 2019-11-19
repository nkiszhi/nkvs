#encoding: utf-8
import requests 
import re
import os

# Cheng Kai
# 
def select(new_content, appeared_content):
	content = appeared_content if appeared_content else new_content 
	return content

def get_torrent_list(content,torrent_dir):
	torrent_paths = []
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
    			with open(torrent_path,'wb') as f:
        			f.write(r.content)
        			f.close()
        			print("文件保存成功")
	else:
		exit("[!]no '%s'"% torrent_dir)
	return torrent_paths
	
	
