# Created stock-scrap.py in /usr/lib/python3.5
# sudo docker cp 1a94fc01b258:/usr/lib/python3.5/stock_values.csv ~/Desktop/

import bs4, urllib, csv, re
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_1 = 'https://es.finance.yahoo.com/quote/%5EIBEX/components?p=^IBEX'
url_2 = 'https://es.finance.yahoo.com/quote/%5ESTOXX50E/components?p=%5ESTOXX50E'
url_3 = 'https://es.finance.yahoo.com/quote/%5EGDAXI/components?p=%5EGDAXI'
url_4 = 'https://es.finance.yahoo.com/quote/%5EFTSE/components?p=%5EFTSE'
url_5 = 'https://es.finance.yahoo.com/quote/%5EGSPC/components?p=%5EGSPC'
url_6 = 'https://es.finance.yahoo.com/quote/%5EDJI/components?p=%5EDJI'
url_7 = 'https://es.finance.yahoo.com/quote/%5EIXIC/components?p=%5EIXIC'

urls = [url_1, url_2, url_3, url_4, url_5, url_6, url_7]

for url in urls:
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    linkData = soup.findAll('tr', attrs={'class': 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s)'})
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
    print (textData[x])

with open('stock_values.csv', 'w', encoding = 'utf-8') as f:
    for val in textData:
        f.write(''.join(val))

#    for x in range(len(linkData)):
#        textData.append(linkData[x].get_text('|'))
#        print(textData[x])

