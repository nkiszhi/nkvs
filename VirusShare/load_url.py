#encoding: utf-8
import requests
import re
import os


def get_html(username,password):
  	global html
        data = {    
    	'username': username,
    	'password': password
}
	headers = {
    	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
}
	login_url = 'https://virusshare.com/processlogin.4n6'
	session = requests.Session()
	resp = session.post(url=login_url,data=data,headers=headers)
	print(resp.text)
	url = 'https://virusshare.com/torrents.4n6'
	resp = session.post(url=url,headers=headers)
	print(resp.status_code)
	html = resp.text
	print(html)
	return html

def get_url_list(content,url_path):
	print(666666)
	f = open(url_path,'w')
	for match in content:
    		f.write(match+'\n')
	f.close()				
	return  content

