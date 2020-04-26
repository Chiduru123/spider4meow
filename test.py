#!/usr/bin/env python
# encoding: utf-8
'''
# Author:        Guo Qi
# File:          test.py
# Date:          2020/4/19
# Description:
'''


import requests
from lxml import etree
url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
print(type(data))
print(data)
exit()
s = etree.HTML(data)
film = s.xpath('//*[@id="content"]/h1/span[1]/text()')
print(film)

