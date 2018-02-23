#coding:utf8
import urllib
import urllib2
import cookielib
import re
import csv
import codecs
from bs4 import BeautifulSoup

wiki = 'https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E7%BC%96%E8%BE%91%E5%99%A8%E6%AF%94%E8%BE%83'
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

name = ""       #名字
creater = ""    #归属
first = ""      #首次公开发布的时间
latest = ""     #最新稳定版本
cost = ""       #售价
licence = ""    #授权条款

table = soup.find("table", {"class" : "sortable wikitable"})

f = open('table.csv', 'w')
csv_writer = csv.writer(f)

td_th = re.compile('t[dh]')

for row in table.findAll("tr"):
    cells = row.findAll(td_th)
    if len(cells) == 6:
        name = cells[0].find(text=True)
        if not name:
            continue
        creater = cells[1].find(text=True)
        first = cells[2].find(text=True)
        latest = cells[3].find(text=True)
        cost = cells[4].find(text=True)
        licence = cells[5].find(text=True)

        csv_writer.writerow([ x.encode('utf-8') for x in [name, creater, first, latest, cost, licence]])

f.close()