from bs4 import BeautifulSoup

import requests
url = "https://www.python.org/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
inputTag = soup.find(attrs={"title": "success-stories"})
output = inputTag['href'][-16:][:15].encode()

fname = "output.yaml"
with open(fname, 'wb') as f:
    f.write(b'link: '+output+b'\n')

############ output #############
#################################
###                           ###
### link: success-stories     ###
###                           ###
#################################