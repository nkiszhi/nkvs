#encoding: utf-8
import requests
import re
import os


def get_html():
    global html
    headers = {
    #假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    #把你刚刚拿到的Cookie塞进来
    'Cookie': 'SID=bevv90v0hfldj2orc52atrgvg1',
}

	session = requests.Session()
	response = session.get('https://virusshare.com', headers=headers)
	load_response = session.get('https://virusshare.com/torrents.4n6', headers=headers)
	print(response.status_code)
	print(load_response.status_code)
	print(1111111111111)
	html = load_response.text
	#for match in re.finditer(r"(?m)<a.*?href=\"(VirusShare_.*?)\"><\/a>", html):
	#    print(match.group(0))
	print(html)
	return html
print(88888888)

def get_url_list(html,url_dir):
    appeared_content = []
    new_content = []
    if (html):
    	if (url_dir):
    		if not os.path.exists(url_dir):
    			os.mkdir(url_dir)
    		url_path = os.path.join(url_dir,"url_list.txt")
    		new_content = re.findall(r"<a.*?href=\"(.*VirusShare_\d{5}.*)\">.*<\/a>",html,re.I)

    		if not os.path.exists(url_path):
    			print(666666)
    			f = open(url_path,'w')
    			for match in new_content:
    				f.write(match+'\n')
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

    		if (appeared_content):
    			print(77777777)
    			f = open(url_path, 'a') 
    			for match in appeared_content:
    				match = str(match)
    				f.write(match+'\n')
                                f.close()
    	else:			
    		exit("[!]no '%s'"% url_dir)
    else:
    	exit("[!]missing website")
    return new_content,appeared_content

if __name__ == "__main__":
	html = get_html()
	get_url_list(html)
