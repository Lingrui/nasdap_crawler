#!/usr/bin/env python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from collections import defaultdict
import simplejson as json

###Company Informnation###
def test_company (table):
    text = pq(table).text()
    return 
def parse_company (bigtable, table):
    bigtable['company'] = pq(table).text()

def test_balance (table):
    text = pq(table).text()
    return "Assets" in text and "Liabilities" in text
def parse_balance (bigtable, table):
    bigtable['balance'] = pq(table).text()
    pass


parser = [(test_company,parse_company),
        (test_balance, parse_balance),
         ]

f = open("goog.out.txt", "w") 
#doc = pq(url ="https://www.nasdaq.com/symbol/c/stock-report")
#doc = pq(url ="https://stockreports.nasdaq.edgar-online.com/goog.html")
#print doc('title')
doc = pq(filename='goog.html')

'''
it = doc('#Table3')
print it.text()
sys.exit(0)

'''
bigtable = {}

for table in doc('table'):
    for test, parse in parser:
        cnt = 0
        if test(table):
            parse(bigtable, table)
            cnt += 1
            pass
        assert cnt == 1
        pass
    pass


print json.dumps(bigtable)
sys.exit(0)

it = iter(doc('table')) #.items()

while True:
    table = next(it)
    if table.attrib.get('id', None) == 'Table3':
        break
table = next(it)
compinfo = {}
for tr in pq(table)('tr'):
    td1, td2 = pq(tr)('td')
    compinfo[pq(td1).text()] = pq(td2).text()
bigtable["Company_Information"] = compinfo
table = next(it)
table = next(it)
table = next(it)
bigtable["desc"] = pq(table).text()


print json.dumps(bigtable)
sys.exit(0)

for xx in doc('table.marginB5px').items():
    print xx.text()

sys.exit(0)


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
