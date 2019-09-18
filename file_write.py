#!/usr/bin/python

import os
path = '/Users/shashis/Desktop/py_train/abc.txt'

fo=open(path)
fo1=open('log_connect.txt','a')
data=fo.readlines()

for record in data:
	result=os.system('ping -c 1 {} > null'.format(record.split(',')[1]))
	if result == 0:
		print ("{} is connected".format(record.split(',')[1]))
	else:
		print ("{} is not connected".format(record.split(',')[1]))
fo.close()
fo1.close()
