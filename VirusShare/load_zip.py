#encoding: utf-8
import os
import time
import transmissionrpc
path = './torrent'
def get_zip_list(torrent_paths,zip_dir):
    print(565656)
    print(torrent_paths)
    if(zip_dir):
        if not os.path.exists(zip_dir):
            os.mkdir(zip_dir)
        zip_dir = os.path.abspath(zip_dir)
	print(zip_dir)
        for torrent_path in torrent_paths:
            torrent_path = os.path.abspath(torrent_path)
            tc = transmissionrpc.Client(address='127.0.0.1',port=9091,user='jackey',password='jackey')
            tc.add_torrent(torrent=torrent_path,download_dir=zip_dir)    
        t = tc.get_torrents()
        torrent_process =[] 
        while set(torrent_process)!=[1]:
	    torrent_process = []
            for i in t:
                print(i.progress)
	        torrent_process.append(i.progress)
            print(torrent_process)	   
            time.sleep(30)
            print("after 30s:")
    else:
        exit("[!]no '%s'"% zip_dir)
    return zip_dir
