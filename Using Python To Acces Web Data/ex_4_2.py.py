# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input("Enter the count: "))
pos=int(input("Enter the position: "))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    s=list()
    t=list()
    for tag in tags:
        link=tag.get('href',None)
        s.append(link)
        y=tag.text
        t.append(y)
    print(s[pos-1])
    print(t[pos-1])
    url=s[pos-1]
