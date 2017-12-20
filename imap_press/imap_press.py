#!/usr/bin/python

import os
import sys
import random
import thread
import threading
import time
import imaplib

sumNum = 0
aliveNum = 0

def Login(user, password):
	global aliveNum
	threadLock.acquire()
	aliveNum = aliveNum + 1
	threadLock.release()
	try:
		M = imaplib.IMAP4("10.10.33.38")
		M.login(user, password)
		while 1:
			M.select()
			threadLock.acquire()
			print user,"select success!"
			threadLock.release()
			time.sleep(random.randint(60, 300))

		M.close()
		M.logout()
	except BaseException, Argument:
		threadLock.acquire()
		print user, Argument
		aliveNum = aliveNum - 1
		threadLock.release()

def Stat():
	global sumNum
	global aliveNum
	while 1:
		time.sleep(5)
		threadLock.acquire()
		print "==================Sum user:", sumNum, " Alive user:", aliveNum, "======================"
		threadLock.release()
	
threadLock = threading.Lock()

try:
	userlist = open("user.list", "r")
	users = {}
	index = 0
	for line in userlist.readlines():
		index = index + 1
		sumNum = sumNum + 1
		line = line.strip('\n')
		userinfo = line.split()
		if len(userinfo) != 2:
			print "user.list line ", index, "format error"
			sys.exit()
		users[userinfo[0]] = userinfo[1]

	thread.start_new_thread(Stat, ())

	index = 0
	for user, password in users.items():
		#index = index + 1
		#if index % 7 == 0:
		#	time.sleep(1)
		#print "user:", user, " pass:", password
		thread.start_new_thread(Login, (user, password))


except BaseException, Argument:
	print Argument

while 1:
	pass
