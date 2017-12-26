#!/usr/bin/python
#-*- encoding:utf-8 -*-

import quopri
import os
import codecs

words = open("words.txt", "r")
for line in words.readlines():
	print line
	line = quopri.encodestring(line)
	line = line.strip('\n')
	line = line.replace("+", "\+")
	line = line.replace("?", "\?")
	print "/" + line + "/\tREJECT"
