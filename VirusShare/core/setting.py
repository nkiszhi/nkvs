import os
import re
from core.attribdict import AttribDict
config = AttribDict()
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
CONFIG_FILE = os.path.join(ROOT_DIR,"virusshare.conf")
def read_config(config_file):
	global config
	if not os.path.isfile(config_file):
		exit("[!]missing configuration file '%s'" % config_file)
	else:
		print "[i] using configuration file '%s'" % config_file
	config.clear()
	content = open(config_file,"rb").read()
	for line in content.split("\n"):
		line = line.strip('\r')
		line = re.sub(r"\s*#.*","",line)
		print(line)
		if line.strip():
			name,value = line.strip().split(' ',1)
			name = name.strip().upper()
			value = value.strip("'\"").strip()
			config[name] = value
	print(config)

			



if __name__ != "__main__":
	read_config(CONFIG_FILE)
		
