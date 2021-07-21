import requests
from bs4 import BeautifulSoup

url = 'https://www.eccj.or.jp/mgr1/test_past/index.html'
res = requests.get(url)

soup = BeautifulSoup(res.content)

links = soup.findAll('a')

link = links[60]
href = link.get('href')

url_new = url + href
url_new

url_new_new =url_new.replace('index.html', '')

print(url_new_new)

import urllib.request
urllib.request.urlretrieve(url_new_new, 'energy1.pdf')