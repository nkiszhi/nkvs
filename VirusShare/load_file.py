#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re
import os

def get_file_list(torrent_paths,zip_dir):
	print(565656)
	print(torrent_paths)
	if (zip_dir):
		if not os.path.exists(zip_dir):
			os.mkdir(zip_dir)
		zip_dir = os.path.abspath(zip_dir)
		transimission_config = subprocess.Popen("transmission-daemon -w " + zip_dir, stdout=subprocess.PIPE, shell=True)
		print(transimission_config.stdout.read())
		#print(787877877)
		for torrent_path in torrent_paths:
			print(torrent_path)
			p=subprocess.Popen("transmission-remote -n jackey:jackey -a " + torrent_path,stdout=subprocess.PIPE,shell=True)
			print(p.poll())
			print(p.stdout.read())
			#p= subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
			#print(p.stdout.read())
			#print(98989898)
	else:
		exit("[!]no '%s'"% zip_dir)
	return zip_dir

	
