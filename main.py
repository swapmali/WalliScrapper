"""
https://www.youtube.com/watch?v=sQFCe_W14js
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import time
from PIL import Image, ImageDraw, ImageFont
import ctypes
import os


print('@author: Swapnil Mali \n\n(Note: New wallpaper is available everyday after 2.00 pm)')
print("Downloading Today's Wallpaper...please wait!!")
res = requests.get('https://bing.wallpaper.pics/')
soup = BeautifulSoup(res.text, 'lxml')
image_box = soup.find('a', {'class': 'cursor_zoom'})
image = image_box.find('img')
link = image['src']

filename = datetime.now().strftime('%d-%m-%y')
urllib.request.urlretrieve(link, '{}.jpg'.format(filename))

# for copyright overlaying text over the image
image = Image.open('{}.jpg'.format(filename))
font_type = ImageFont.truetype('fonts/Quicksand-Bold.otf', 44)
draw = ImageDraw.Draw(image)
draw.text(xy=(800, 1000), text='© Swapnil Mali', fill=(0,0,0), font=font_type)
# image.show()
image.save('{}.jpg'.format(filename))

print("\n\n-------------------------------------------\nDone..New wallpaper saved as '{}.jpg'\n-------------------------------------------".format(filename))
time.sleep(1)
# set new image as desktop background
directory = os.getcwd()
# print(directory)
image_path = '{}\{}.jpg'.format(directory, filename)
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

print("\nSetting new Wallpaper..".format(filename))
time.sleep(2)
print("Done..Closing this window")

time.sleep(2)
