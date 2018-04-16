#!/usr/bin/env python3
import bs4, os, urllib, csv, re, http.cookiejar
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

stocks = ['^IBEX', '^STOXX50E', '^GDAXI', '^FTSE', '^GSPC', '^DJI', '^IXIC']
base_url = 'https://es.finance.yahoo.com/quote/'
historic_url = '/history?p='
#cj = http.cookiejar.CookieJar()
#cj.load(os.path.join(os.environ["HOME"], ".netscape/cookies.txt"))

#def __init__(self, stocks, cookie):
#    self.stocks = []
#    self.cookie = http.cookiejar.CookieJar()

for stock in stocks:
    cj = http.cookiejar.CookieJar()
    browser = webdriver.Firefox()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #urllib.request.install_opener(opener)
    #page = urllib.request.urlopen(base_url+stock+historic_url+stock)
    #page = opener.open("https://es.finance.yahoo.com/quote/^STOXX50E/history?p=^STOXX50E")
    url = base_url+stock+historic_url+stock
    browser.get(url)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    page = opener.open(url)
    soup = BeautifulSoup(browser.page_source.decode('utf-8', 'ignore'), 'html.parser')
    linkData = soup.findAll('tr', attrs={'class': 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'})
textData = []

for x in range(len(linkData)):
    td=linkData[x].findAll('td', attrs={'class' : re.compile('^Py')})
    res = ''
    for y in range(len(td)):
        if y==0:
            res = td[y].get_text()
        else:
            res = res + '|' + td[y].get_text()
    textData.append(res+'\n')
    #print (textData[x])

with open('/data/stock_values.csv', 'w', encoding = 'utf-8') as f:
    for val in textData:
        f.write(''.join(val))
