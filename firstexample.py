#!/usr/bin/env python3

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='http://www.carters.com/carters-baby-boy'
#opening connection, grabbing the page
uClient=uReq(my_url)
#sets the content into a variable
page_html=uClient.read()
uClient.close()
#html pasing
page_soup=soup(page_html,"html.parser")
print(page_soup.prettify()[0:1000])
#page_soup.div
#page_soup.findAll("div",{"class":"product-name"})
#tmp= soup.findAll('ul', {'class' : 'Whs-nw M-0 items'})
#for i in tmp:
#    print(i.get_text())

