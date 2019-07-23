# Standard library imports
import os
import re
import json

# 3rd party imports
from bs4 import BeautifulSoup
from parsel import Selector


# Create output list
output = []

# Function to load an offer file data from offer catalog
def load_offer(_offer):
    file_name = os.path.join('offers', _offer)
    with open(file_name, 'r', encoding="utf-8") as _file_in:
        _data = _file_in.read()
    return _data

# Function to get required data of the corresponding offer
def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')

    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=_data)

    # Search for required data

    # Search for offer_id
    filtered = selector.xpath('//*[@id="offer--searcher"]/div[3]/header/div/div[1]/div/small/text()[2]').get()
    print("id_oferty : ", filtered)
    offers_data['id_oferty'] = filtered

    # Search for location
    filtered = selector.xpath('/html/body/div[1]/div[1]/header/nav/span[2]/text()').get()
    filtered = filtered.strip()
    print("lokalizacja : " + filtered)
    offers_data['lokalizacja'] = filtered

    # Search for title
    filtered = selector.css('head > title:nth-child(19)::text').get()
    print("tytul : " + filtered)
    offers_data['tytul'] = filtered

    # Search for price per person
    filtered = selector.xpath('//*[@id="gnc--ttip--toggle"]/text()[2]').get()
    print("cena_za_osobe : " + filtered)
    offers_data['cena_za_osobe'] = filtered

    # Search for total price
    filtered = selector.xpath('//*[@id="offer--searcher"]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/span/text()[1]').get()
    print("cena_za_calosc : " + filtered)
    offers_data['cena_za_calosc'] = filtered

    # Search for html
    # filtered = selector.css('.canonical::attr(href)').get()
    filtered = selector.css('head > link:nth-child(21)::attr(href)').get()
    print("html : " + filtered)
    offers_data['html'] = filtered

    # Get table where offer details are stored
    filtered = soup.find_all(attrs={"class": "accordion-tabs accordion-tabs-offer accordion--tabs"})
    filtered_string = str(filtered)

    # Search for offer text
    offers_data['tresc_oferty'] = filtered_string

# Create a json file to store the offers data
with open('stored_offers_data.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('offers')
    for offer in offers:
        offers_data = {}
        # Print offer file name
        print(offer)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        get_details(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
