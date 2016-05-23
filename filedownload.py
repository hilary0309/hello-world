import requests
from bs4 import BeautifulSoup
import os

url = 'http://web.mta.info/developers/turnstile.html'
html = requests.get(url)

fileurl = 'http://web.mta.info/developers/data/nyct/turnstile/'
soup = BeautifulSoup(html.text,"html.parser")

for link in soup.find_all('a'):
    href = link.get('href')

    if not href is None: 
        if not href.startswith('http'):
            filename = os.path.split(href)[1]
            if href.endswith('.txt') and filename.startswith('turnstile_13'):  
                with open(filename, 'wb') as f_output:
                    f_output.write(requests.get(fileurl+filename).content)
