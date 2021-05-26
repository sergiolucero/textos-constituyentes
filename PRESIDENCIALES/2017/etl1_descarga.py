import requests, wget
from bs4 import BeautifulSoup

bs=BeautifulSoup(requests.get('https://www.servel.cl/programas-de-candidaturas-a-presidente-de-la-republica/').text)
links=[link['href'] for link in bs.find_all('a') if 'Programa' in link['href']]

for link in links:
    wget.download(link)
