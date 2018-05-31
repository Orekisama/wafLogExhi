#!/usr/bin/python
# -*- coding: utf-8 -*-

keyWord = []

with open('keyWordAll.txt', 'r') as keyWordAll:
	for line in keyWordAll:
		keyWord.append(line.strip('\n'))
with open('waf_audit.log', 'r') as logFile:
	logFile_read = logFile.read()
	for num in range(0, len(keyWord)):
		keyWord_s = keyWord[num]
		logFile_witre, logFile_read = logFile_read.split(keyWord_s)
		result = open('/usr/local/nginx/html/auditLog/%s'% keyWord[num-1] + '.txt', 'w')
		result.write(logFile_witre)
		result.close()
