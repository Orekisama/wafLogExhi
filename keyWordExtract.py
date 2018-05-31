#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('waf_audit.log', 'r') as f1, open('keyWordAll.txt', 'w') as f2:
    for line in f1.readlines():
        if '---' in line:
            f2.write(line.strip('\n').strip('-') + '\n')