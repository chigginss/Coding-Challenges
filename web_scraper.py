"""Web Scraper in Python using Beautiful Soup"""

import urllib2
from bs4 import BeautifulSoup

quote = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote)
soup =  BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class':'price'})
print name_box