#!/usr/bin/env python
# encoding=utf8
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from collections import defaultdict
import simplejson as json

###Company Informnation###
def test_company (table):
    text = pq(table).text()
    return "Address:" in text 
def parse_company (bigtable, table):
    bigtable['Company_Information'] = pq(table).text()
    pass

####
def test_balance (table):
    text = pq(table).text()
    return "Assets" in text and "Liabilities" in text
def parse_balance (bigtable, table):
    '''
    i = 0
    bigdic = {}
    rows = []
    ass = {}
    lia = {}
    sto = {}
    col1 = col2 = col3 = col4 = {}
    cn1 = cn2 = cn3 = cn4 = ''
 
    for tr in pq(table)('tr'):
        td1,td2,td3,td4 = pq(tr)('td')
        if i == 0:
            cn1 = pq(td2).text()
            cn2 = pq(td3).text()
            cn3 = pq(td4).text()
            cn4 = pq(td5).text()
            pass
        elif i < 7:
            col1[pq(td1).text()] = pq(td2).text()    
            col2[pq(td1).text()] = pq(td3).text()    
            col3[pq(td1).text()] = pq(td4).text()    
            col4[pq(td1).text()] = pq(td5).text()    
            pass
        elif i > 8:
            ass[pq(td1).text()] = pq(td2).text()    
            liq[pq(td1).text()] = pq(td2).text()    
            pass
        i += 1 
        pass
    bigdic["Asset"] = ass
    bigdic["Liquidity"] = liq
    bigdic["Leverage"] = lev
    rows.append(bigdic)
    '''
    bigtable['Balance Sheet(Millions)'] = pq(table).text()
    pass

######
def test_description (table):
    text = pq(table).text()
    return "Primary SIC Code" in text
 
def parse_description(bigtable,table):
    bigtable['Description of Business'] = pq(table).text()
    pass

def test_pershare(table):
    text = pq(table).text()
    return "12-mos Rolling EPS" in text and "P/E Ratio" in text

def parse_pershare(bigtable,table):
    i = 0
    heads = []
    rows = []
    #print (pq(table).text())
    for tr in pq(table)('tr'):
        #print(tr.text)
        if i == 0:
            for td in pq(tr)('td'):
                #print (pq(td).text())
                heads.append(pq(td).text())
                pass
            pass
        else:
            contents = []
            h = {}
            for td in pq(tr)('td'):
                contents.append(pq(td).text())
                pass
            for head,content in zip(heads,contents):
                #print (head,content)
                h[head] = content
                pass
            rows.append(h)
        i += 1 
        pass

    bigtable['Per Share Overview'] = rows 
    #bigtable['Per Share Overview'] = pq(table).text()
    pass

def test_key(table):
    text = pq(table).text()
    return "Leverage" in text and "Asset Utilization" in text 

def parse_key(bigtable,table):
    i = 0
    year = ''
    bigdic = {}
    rows = []
    pro = {}
    lev = {}
    ass = {}
    liq = {}
    for tr in pq(table)('tr'):
        td1,td2,td3,td4 = pq(tr)('td')
        if i == 0:
            year = pq(td2).text()
            pass
        elif i < 8:
            pro[pq(td1).text()] = pq(td2).text()    
            lev[pq(td3).text()] = pq(td4).text()    
            pass
        elif i > 8:
            ass[pq(td1).text()] = pq(td2).text()    
            liq[pq(td1).text()] = pq(td2).text()    
            pass
        i += 1 
        pass
    bigdic["year"] = year
    bigdic["Profitability"] = pro
    bigdic["Leverage"] = lev
    bigdic["Asset Utilization"] = ass
    bigdic["Liquidity"] = liq
    rows.append(bigdic)
    #bigtable['Key Financial Ratios and Statistics'] = pq(table).text()
    bigtable['Key Financial Ratios and Statistics'] = rows
    pass

def test_income(table):
    text = pq(table).text()
    return "Total Revenues(Net Sales)" in text and "Selling & Admin Exps" in text 

def parse_income(bigtable,table):
    i = 0
    bigdic = {}
    rows = []
    col1 = col2 = col3 = col4 = {}
    cn1 = cn2 = cn3 = cn4 = ''
    for tr in pq(table)('tr'):
        td1,td2,td3,td4,td5 = pq(tr)('td')
        if i == 0:
            cn1 = pq(td2).text()
            cn2 = pq(td3).text()
            cn3 = pq(td4).text()
            cn4 = pq(td5).text()
            pass
        else:
            col1[pq(td1).text()] = pq(td2).text()    
            col2[pq(td1).text()] = pq(td3).text()    
            col3[pq(td1).text()] = pq(td4).text()    
            col4[pq(td1).text()] = pq(td5).text()    
            pass
        i += 1 
        pass
    bigdic[cn1] = col1
    bigdic[cn2] = col2
    bigdic[cn3] = col3
    bigdic[cn4] = col4
    rows.append(bigdic)
    bigtable['Income Statement(Millions)'] = rows 
    #bigtable['Income Statement(Millions)'] = pq(table).text()
    pass

def test_cash(table):
    text = pq(table).text()
    return "Operating Activities" in text and "Investing Activities" in text 

def parse_cash(bigtable,table):
    i = 0
    heads = []
    rows = []
    #print (pq(table).text())
    for tr in pq(table)('tr'):
        #print(tr.text)
        if i == 0:
            for td in pq(tr)('td'):
                #print (pq(td).text())
                heads.append(pq(td).text())
                pass
            pass
        else:
            contents = []
            h = {}
            for td in pq(tr)('td'):
                contents.append(pq(td).text())
                pass
            for head,content in zip(heads,contents):
                #print (head,content)
                h[head] = content
                pass
            rows.append(h)
        i += 1 
        pass
    bigtable['Cash Flow Summary(Millions)'] = rows 
    #bigtable['Cash Flow Summary(Millions)'] = pq(table).text()
    pass

def test_annual(table):
    text = pq(table).text()
    return "Growth Rates" in text and "Net Income" in text 

def parse_annual(bigtable,table):
    i = 0
    heads = []
    rows = []
    #print (pq(table).text())
    for tr in pq(table)('tr'):
        #print(tr.text)
        if i == 0:
            for td in pq(tr)('td'):
                #print (pq(td).text())
                heads.append(pq(td).text())
                pass
            pass
        else:
            contents = []
            h = {}
            for td in pq(tr)('td'):
                contents.append(pq(td).text())
                pass
            for head,content in zip(heads,contents):
                #print (head,content)
                h[head] = content
                pass
            rows.append(h)
        i += 1 
        pass
    bigtable['Annual Summary Data(Millions)'] = rows
    #bigtable['Annual Summary Data(Millions)'] = pq(table).text()
    pass

def test_stock(table):
    text = pq(table).text()
    return "No. Owners" in text and "Shares Held (000s)" in text 

def parse_stock(bigtable,table):
    i = 0
    heads = []
    rows = []
    #print (pq(table).text())
    for tr in pq(table)('tr'):
        #print(tr.text)
        if i == 0:
            for td in pq(tr)('td'):
                #print (pq(td).text())
                heads.append(pq(td).text())
                pass
            pass
        else:
            contents = []
            h = {}
            for td in pq(tr)('td'):
                contents.append(pq(td).text())
                pass
            for head,content in zip(heads,contents):
                #print (head,content)
                h[head] = content
                pass
            rows.append(h)
        i += 1 
        pass
    bigtable['Stock Ownership'] = rows 
    #bigtable['Stock Ownership'] = pq(table).text()
    pass

parser = [(test_balance, parse_balance), 
        (test_company,parse_company),
        #(test_description,parse_description),
        (test_pershare,parse_pershare),
        (test_key,parse_key),
        (test_income,parse_income),
        (test_cash,parse_cash),
        (test_annual,parse_annual),
        (test_stock,parse_stock),
        ]

def get_sec(symbol):
    '''
    #f = open("goog.out.txt", "w") 
    #doc = pq(url ="https://www.nasdaq.com/symbol/c/stock-report")
    doc = pq(url ="https://stockreports.nasdaq.edgar-online.com/goog.html")
    doc = pq(filename='goog.html')

    it = doc('#Table3')
    print it.text()
    sys.exit(0)
    '''
    doc = pq(url ="https://stockreports.nasdaq.edgar-online.com/"+symbol+".html")
    bigtable = {}
    i = 0  #skip the first table 
    j = 0  #for description of business table
    for table in doc('table'):
        if i>0:
            cnt = 0
            for test, parse in parser:
                #cnt = 0
                if test(table):
                    parse(bigtable, table)
                    cnt += 1
                    pass
                pass
            if j == 2:
                parse_description(bigtable,table)
                j += 1 
                pass

            if test_description(table):
                j += 1
            elif j == 1:
                j += 1
                pass
            assert cnt <= 1
            pass
        i += 1 
        pass


    #print json.dumps(bigtable)
    #pass
    return json.dumps(bigtable)
'''
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
'''
if __name__ == '__main__':
    #get_sec('goog')
    pass
    
