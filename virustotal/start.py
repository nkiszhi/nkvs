#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time

from query_label_from_sha256 import get_label

from get_sha256 import get_sha256

sha256_data = os.path.abspath(os.path.join(os.path.dirname(__file__),'../virusshare/sha256_data'))

#get sha256 and rename
get_sha256(sha256_data)
#get label
get_label()



