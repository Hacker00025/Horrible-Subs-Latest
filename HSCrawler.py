import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def hs_latest():
    anime = set()
    while True:
        url = 'https://horriblesubs.info/api.php?method=getlatest'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features='html.parser')
        b = soup.find_all('li')
        latest = []
        nt = False
        for listitem in b:
            c = listitem.find('a')
            d = c.find('strong')
            f = (c.contents[1] + d.string)
            latest.append(f)
        for z in latest:
            if z not in anime:
                print(z)
                nt = True
        for z in latest:
            anime.add(z)
        if nt:
            print(datetime.now())
            nt = False
        time.sleep(120)

hs_latest()