import requests
import json
import bs4
import urllib2
import gzip
import codecs
import re

#r = requests.get("http://vietnamnet.vn/jsx/loadmore/?domain=desktop&c=the-gioi&p=5&s=10")
#soup = bs4.BeautifulSoup(r.content,'lxml')
##print(r.content)
#test= soup.prettify(formatter="minimal")


URL = 'http://vietnamnet.vn/jsx/loadmore/?domain=desktop&c=the-gioi&p=1&s=50'

mk_js = requests.get(URL)
urls = re.findall('http://vietnamnet.vn(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', mk_js.content)

print(urls)

print('test')

