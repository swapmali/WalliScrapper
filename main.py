"""
Inspired by:  https://www.youtube.com/watch?v=sQFCe_W14js
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import time
from PIL import Image, ImageDraw, ImageFont
import ctypes
import os
import shutil
import socket
import sys


def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


if __name__ == "__main__":
    # check internet connection
    while True:
        #
        if not is_connected("www.google.com"):
            print("@author: Swapnil Mali \nPlease check your internet connection, will try again after 30 seconds..")
            time.sleep(30)
            continue

        # move shortcut to main.exe to startup folder
        try:
            # get user name
            user = os.getlogin()
            path = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main - Shortcut.lnk'.format(user)
            # print(path)
            shutil.move(r'main - Shortcut.lnk', path)
        except FileNotFoundError:
            pass

        # just credit and copyright stuff
        print('@author: Swapnil Mali \n\n(Note: New wallpaper is available everyday after 2.00 pm)')
        print("Downloading Today's Wallpaper...please wait!!")

        # get image link from the website page
        res = requests.get('https://bing.wallpaper.pics/')
        soup = BeautifulSoup(res.text, 'lxml')
        image_box = soup.find('a', {'class': 'cursor_zoom'})
        image = image_box.find('img')
        link = image['src']

        # download and save the image
        filename = datetime.now().strftime('%d-%m-%y')
        urllib.request.urlretrieve(link, '{}.jpg'.format(filename))

        # for copyright overlaying text over the image
        image = Image.open('{}.jpg'.format(filename))
        font_type = ImageFont.truetype('fonts/Quicksand-Bold.otf', 44)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(800, 1000), text='© Swapnil Mali', fill=(0, 0, 0), font=font_type)
        # image.show()
        image.save('{}.jpg'.format(filename))

        print("\n\n-------------------------------------------\nDone..New wallpaper saved as '{}.jpg'\n-------------------------------------------".format(filename))
        time.sleep(1)

        # set new image as desktop background
        directory = os.getcwd()
        image_path = '{}\{}.jpg'.format(directory, filename)
        print("\nSetting new Wallpaper..".format(filename))
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        time.sleep(2)

        print("Done..Closing this window")
        time.sleep(2)
        sys.exit()