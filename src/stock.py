#!/usr/bin/env python3
import bs4, os, urllib, csv, re, time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup as bs

# Define browser
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"
browser = webdriver.Firefox(capabilities=caps)

# Define URLs of interest
stocks = ['^IBEX', '^STOXX50E', '^GDAXI', '^FTSE', '^GSPC', '^DJI', '^IXIC']
base_url = 'https://es.finance.yahoo.com/quote/'
historic_url = '/history?p='

# Write headers to csv file
with open('/data/stock_values.csv', 'w', encoding = 'utf-8') as f:
    fields=['stock','date','open', 'max', 'min', 'close', 'adj close', 'volume']
    writer = csv.writer(f)
    writer.writerow(fields)

# Iterate through stock array
for stock in stocks:
    url = base_url+stock+historic_url+stock
    browser.get(url)
    # Scroll down and wait until all values are loaded
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollTo(0, 50000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 50000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 50000);")
    # Once the page is fully scrolled, grab the source code
    source_data = browser.page_source

    # Parse html data using bs
    soup = bs(source_data, 'html.parser')
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
        textData.append(stock+'|'+res+'\n')

    # Write scrapped data to csv file
    with open('/data/stock_values.csv', 'a', encoding = 'utf-8') as f:
        for val in textData:
            val = val.replace(',', '.')
            f.write(''.join(val.replace('|', ',')))

# Close browser
browser.close()

# Geckodriver
# wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz
# tar -xvzf geckodriver*
# chmod +x geckodriver
# export PATH=$PATH:$(pwd)/geckodrive
