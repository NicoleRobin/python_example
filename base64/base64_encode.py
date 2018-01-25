#!/usr/bin/python
#-*- encoding:utf-8 -*-

import base64
import os
import re

words = open("words.txt", "r")
for line in words.readlines():
	line = line.strip('\n')
	#print line
	line = base64.b64encode(line)
	line = line.strip('=')
	line = line.replace("/", "\/")
	line = line.replace("+", "\+")
	print "/^Subject:.*" + line + "/\tREJECT"
