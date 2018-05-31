#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('waf_audit.log', 'r', encoding='utf8') as f1, open('keyWordAll.txt', 'w', encoding='utf8') as f2:
    for keyword in f1.readlines():
        if '---' in keyword:
            f2.write(line.strip('\n').strip('-') + '\n')