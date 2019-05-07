# Standard library imports
import json


# Create object representing vacation offers and input required data
with open('stored_offers_data.json', 'r', encoding="utf-8") as data_file:
    reader = json.load(data_file)
    for single_offers_data in reader:
        tresc_oferty = single_offers_data['tresc_oferty']
        # offer_data = Offer(**single_offers_data)
        html = single_offers_data['html']
        if all(i in tresc_oferty for i in ['brodzik', 'piaszczysta plaża', 'dla dzieci', 'animacje dla dzieci']) == True:
            print(html)

slowa_klucz = ['dla rodzin z dziećmi poniżej 5 roku życia', 'brodzik', 'piaszczysta plaza', 'plac zabaw', 'kacik dla dzieci', 'animacje dla dzieci']