from bs4 import BeautifulSoup
import requests
url = "http://www.carters.com/carters-toddler-boy-graphic-tees"

# add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")
print (soup.h1)