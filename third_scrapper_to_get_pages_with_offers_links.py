# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Create required lists
url_list = ['https://www.travelplanet.pl/wczasy/oferty/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/2/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/3/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/4/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/5/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/6/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/7/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/8/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/9/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/10/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            ]
links_data_list = []

# Function to get offer links
def get_links(url):
    # Get page from url
    response = requests.get(url)
    content = response.text

    # Get offer links from url
    selector = Selector(text=content)
    links_data = selector.css('.oi-heading > a::attr(href)').getall()
    links_data_list.append(links_data)

for url in url_list:
    get_links(url)

# Create a json file to store the page data
with open('stored_links.json', 'w', encoding="utf-8") as stored_links:
    # Save offers links to json's file
    json.dump(links_data_list, stored_links, indent=4, ensure_ascii=False)