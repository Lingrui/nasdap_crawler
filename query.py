# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from collections import defaultdict

f = open("goog.out.txt", "w") 
#doc = pq(url ="https://www.nasdaq.com/symbol/c/stock-report")
doc = pq(url ="https://stockreports.nasdaq.edgar-online.com/goog.html")
#print doc('title')
data = doc('tr')
i = 0
for tr in data.items():
    #temp = tr('td').text()
    temp = tr('tr')
    for aaaa in temp.items():
        ttt = aaaa('td')
        cccc = ''
        for t in ttt.items():
            cccc = cccc+t.text()+"\t"
        #print >>f, t.text()
        print >>f, cccc
    i+=1
    #print >>f, i,'+'*50

f.close()
