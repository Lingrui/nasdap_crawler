import urllib2
from bs4 import BeautifulSoup 
import requests,re
'''
report = urllib2.Request("https://www.nasdaq.com/symbol/c/stock-report")
page = urllib2.urlopen(report).read()
print page
'''
URL = "https://www.nasdaq.com/symbol/c/stock-report"
data = requests.get(URL).content
soup = BeautifulSoup(data,"html.parser")
#Stock Report Details###########3
name = soup.find('table',attrs={'class':'marginB5px'})
d = []
for idx,tr in enumerate(name.find_all('tr')):
	tds = tr.find_all('td')
	tas = tr.find_all('a')
	ths = tr.find_all('th')
	d.append(tds[0].contents[0])
	d.append(tds[1].contents[0])
	#print tas[0].contents[0]
	#print ths[0].contents[0]
print d 
#Today's market activity
market = soup.find()
#Company Information 
tables =soup.find('table',attrs={'border':'1'})
