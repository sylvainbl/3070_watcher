import requests
from bs4 import BeautifulSoup
import time
import ctypes


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


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def analyse_prices(array_prices, limit):
    min_price = min(array_prices)
    if min_price < limit:
        Mbox("3070 EN STOCK", "ELLE EST DE RETOUR A " + str(min_price) + " €", 0)
        return True
    return False


if __name__ == "__main__":
    found = False
    while found == False:
        found = analyse_prices(find_prices(), 670)
        if not found:
            time.sleep(60)
