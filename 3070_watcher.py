import requests
from bs4 import BeautifulSoup


def find_prices():
    URL = 'https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?onlyInStock=true&fv_gpu.chip=NVIDIA%20RTX%203070'
    page = requests.get(URL)

    array_prices = []

    soup = BeautifulSoup(page.content, 'html.parser')

    prices = soup.find_all(
        class_='font-weight-bold text-secondary w-100 d-block h1 mb-2')

    for price in prices:
        price_elem = price.find('span')
        array_prices.append(int(price_elem.text))

    return array_prices


def analyse_prices(array_prices, limit):
    if min(array_prices) < limit:
        return True
    return False


print(analyse_prices(find_prices(), 580))
