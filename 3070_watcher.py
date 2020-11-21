import requests
from bs4 import BeautifulSoup


URL = 'https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?onlyInStock=true&fv_gpu.chip=NVIDIA%20RTX%203070'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

prices = soup.find_all(
    class_='font-weight-bold text-secondary w-100 d-block h1 mb-2')


for price in prices:
    price_elem = price.find('span')
    print(price_elem.text, end='\n'*2)
