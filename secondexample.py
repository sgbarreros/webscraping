#!/usr/bin/env python3
import urllib
from bs4 import BeautifulSoup
response = urllib.urlopen('http://finance.yahoo.com/')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
tmp= soup.findAll('ul', {'class' : 'Whs-nw M-0 items'})
for i in tmp:
    print(i.get_text())
