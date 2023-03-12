from bs4 import BeautifulSoup
import requests
import numpy
import csv
from datetime import datetime

LINK = ""

def get_prices_by_link(link):
    #get source
    r = requests.get(link)

    #parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')

    #find the lists of objects of the search of ebay
    search_results = page_parse.find("ul", {"class":"srp-results"}).find_all("li",{"class":"s-item"})

    item_prices = []

    for result in search_results:
        price_as_text = result.find("span", {"class":"s-item__price"}).text
        if "to" in price_as_text:
            continue
        price = float(price_as_text[1:].replace(","""))
        item_prices.append(price)

    return item_prices

