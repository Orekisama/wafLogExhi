#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option('max_colwidth', 200)
def convertToHtml(result,title):
    #将数据转换为html的table
    #result是list[list1,list2]这样的结构
    #title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html('table_no_button.html', index=False, col_space=100)
    return h

timestamp = []  
with open('txtFile/timestamp.txt') as f1:
	for line in f1.readlines():
		timestamp.append(line.strip('\n'))
	  
host = []  
with open('txtFile/host.txt') as f2:
	for line in f2.readlines():
		host.append(line.strip('\n'))

uri = []  
with open('txtFile/uri.txt') as f3:
	for line in f3.readlines():
		uri.append(line.strip('\n'))

keyWordB = []  
with open('txtFile/keyWordB.txt') as f5:
	for line in f5.readlines():
		keyWordB.append(line.strip('\n'))

keyWordF = []  
with open('txtFile/keyWordF.txt') as f7:
	for line in f7.readlines():
		keyWordF.append(line.strip('\n'))

keyWordH = []  
with open('txtFile/keyWordH.txt') as f8:
	for line in f8.readlines():
		keyWordH.append(line.strip('\n'))


if __name__ == '__main__':
	result = [timestamp, host, uri, keyWordB, keyWordF, keyWordH]
	title = ['TimeStamp', 'Host', 'uri', 'Request Header',  'Response Header', 'WAF info']
	print(convertToHtml(result,title))
	i = 1
	with open(r"keyWordButton.txt", 'r', encoding='utf8')as b:
		with open(r"table_no_button.html", 'r', encoding='utf8')as a:
			a_read = a.read()
			for line in b:
				b_line = line.strip('\n')
				b_line_re = '''<input type="button" onclick="openDiv('div%d')" class="btn" value="%s"/>''' %(i, b_line)
				a_read = a_read.replace(b_line,b_line_re)
				i += 1
			result = open("table_button.html", 'w')
			result.write(a_read)
			result.close()
	
	j = 1
	with open(r"keyWordButton.txt", 'r', encoding='utf8')as c, open('frame.txt', 'w', encoding='utf8') as d:
		lines = c.readlines()
		for frame in lines:
			frame = frame.strip('\n')
			d.write('''<div id="div%d" class="opendiv" style="width: 80%%;height: 500px;">\n'''% j)
			d.write('''<iframe src="auditLog/%s.txt" align="middle" frameborder="none" scrolling="auto" style="width: 100%%; height: 100%%;"></iframe>\n'''% frame)
			d.write('''</div>\n''')
			j += 1
		d.write('''<div id="bgdiv"></div>\n''')
	
	file_button = open( "table_button.html", "r", encoding='utf8')
	file_div = open("frame.txt","r", encoding='utf8')
	content = file_button.read()
	contentadd = file_div.read()
	file_button.close()
	file_div.close()
	pos = content.find( "</tbody>" )
	if pos != -1:
		content = content[:pos] + contentadd + content[pos:]
		file = open( "table_button.html", "w", encoding='utf8')
		file.write(content)
		file.close()
		print("OK")