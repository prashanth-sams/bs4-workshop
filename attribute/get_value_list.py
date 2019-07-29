from bs4 import BeautifulSoup

import requests
url = "https://www.python.org/"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

fname = "output.yaml"
with open(fname, 'w') as f:
    for link in soup.find_all('a'):
        f.write(str(link.get('href')) + '\n')
    
############ output #############
#################################
###                           ###
###     /community/irc/       ###
###     /about/               ###
###     /about/apps/          ###
###     /about/quotes/        ###
###     /about/gettingstarted/###
###     /about/help/          ###
###     ....                  ###
#################################