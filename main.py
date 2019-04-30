"""
https://www.youtube.com/watch?v=sQFCe_W14js
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import time
print('(Note: New wallpaper is available everyday after 2.00 pm)')
print("Downloading Today's Wallpaper...please wait!!")
res = requests.get('https://bing.wallpaper.pics/')
soup = BeautifulSoup(res.text, 'lxml')
image_box = soup.find('a', {'class': 'cursor_zoom'})
image = image_box.find('img')
link = image['src']

filename = datetime.now().strftime('%d-%m-%y')
urllib.request.urlretrieve(link, '{}.jpg'.format(filename))
print('-----Done------')
time.sleep(5)