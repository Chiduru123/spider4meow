#!/usr/bin/env python
# encoding: utf-8
'''
# Author:        Guo Qi
# File:          main.py
# Date:          2020/4/18
# Description:   一个豆瓣车的spider
'''

from urllib.parse import urlencode
from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup
import re
import datetime
import os
import sys
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
import utils.tools as tools
tool = tools.util()

delta = datetime.timedelta(days=-1)
time_threshold = (datetime.datetime.now() + delta).strftime('%Y-%m-%d %H:%M:%S')
today = datetime.datetime.now().strftime('%Y%m%d')
histInfo_file = os.path.join(root, 'data/histInfo_{}.txt'.format(today))


class Conn(object):
    def __init__(self, params='', url=''):
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        if url != '':
            self.base_url = url
        else:
            self.base_url = 'default-url'
        self.context = ssl._create_default_https_context()
        if params != '':
            self.url = '{}?{}'.format(self.base_url, urlencode(params))
        else:
            self.url = self.base_url
        self.response = Request(self.url, headers={'User-agent': self.ua})


# main
hist_ids = []
if os.path.exists(histInfo_file):
    with open(histInfo_file, 'r') as fr:
        for line in fr.readlines():
            id = line.strip('\r\n').split('\t')[0]
            hist_ids.append(id)

res_list = []
msg_list = []
urls = [
    'url1',
    'url2'
    ]

for url in urls:
    conn = Conn(url=url)
    with urlopen(conn.response, context=conn.context) as res:
        data =BeautifulSoup(bytes.decode(res.read()), 'html.parser')
        recs = data.find_all('tr',  class_='pl')

        for rec in recs:
            rec = rec.find_all('td')
            href = rec[0].find_all('a', class_="")[0]['href']
            id = href.split('/')[-2]
            if id in hist_ids:      # 筛除历史已有车信息
                continue
            time = rec[1]['title']
            if time < time_threshold:
                continue
            title = re.sub('\n', '', rec[0].find_all('a')[0]['title'])

            res_list.append('\t'.join([id, href, title]))


if len(res_list) > 0:
    print('Get info cnt: {}'.format(len(res_list)))
    tool.send_email('\n'.join(res_list))
    if len(msg_list) > 0:
        tool.send_messge(' '.join(msg_list))

    with open(histInfo_file, 'a') as fw:
        fw.write('\n'.join(res_list) + '\n')
