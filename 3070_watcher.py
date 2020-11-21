import requests
from bs4 import BeautifulSoup

URL = 'https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?onlyInStock=true&fv_gpu.chip=NVIDIA%20RTX%203070'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
