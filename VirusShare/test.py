#/usr/bin/python
#encoding:utf-8
import subprocess
import os

user = "jackey"
password = "jackey"
zip_path = "./zip"

if not os.path.exists(zip_path):
	os.mkdir(zip_path)
zip_path = os.path.abspath(zip_path)
print(zip_path)
transimission_config = subprocess.Popen("transmission-daemon -w "+zip_path,stdout=subprocess.PIPE,shell=True)
print(transimission_config.stdout.read())
torrent_path = "/home/jackey/VirusShare/torrent"
files = os.listdir(torrent_path)

for file in files:
	file_path = os.path.join(torrent_path,file)
	print(file_path)
	print(type(file))
	print(file)
	#p=subprocess.Popen("transmission-remote -n jackey:jackey -a "+file_path,stdout=subprocess.PIPE,shell=True)
	flag = 0
	p=subprocess.Popen("transmission-remote -n jackey:jackey -a "+file_path,stdout=subprocess.PIPE,shell=True)
	while not flag:
		#print(p.stdout.read())
		print(p.poll())
		print(121212)
		flag = p.poll()
	#print(p.communicate())
	#p= subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
	#print(p.stdout.read())
	print(1111111111)
