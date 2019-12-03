import os
from multiprocessing import Process,Pool
def get_url_list():
    ret = []
    with open('./url_list.txt','r') as f:
        for line in f:
            ret.append(line.strip('\n'))
    return ret
def get_apk(url):
    sha256_name = url.split('=')[-1].lower()
    apk_path = os.path.join('./apk',sha256_name[0],sha256_name[1],sha256_name[2],sha256_name[3])
    print(apk_path)
    if not os.path.exists(apk_path):
        os.makedirs(apk_path)
    apk_path = os.path.join(apk_path,sha256_name)
    p = os.popen('wget -c -O '+apk_path+' "'+url+'"'+' -o ./log')
    print(p)
def main():
    child = get_url_list()
    print('Parent process %s.' %os.getpid())
    p=Pool(8)
    for each in child:
        p.apply_async(get_apk,args=(each,))
    p.close()
    p.join()
if __name__ == '__main__':
    main()
    
