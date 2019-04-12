# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Create required lists
url_list = ['https://www.travelplanet.pl/wczasy/oferty/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dojazd=F&dzieci=2&wyzywienie=1&czas=6:8',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/2/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/3/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/4/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/5/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/6/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/7/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/8/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/9/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/10/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            'https://www.travelplanet.pl/wczasy/oferty/grecja/11/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dzieci=2&czas=6:8&wyzywienie=1&dojazd=F&sortowanie=1&kolejnosc=up&limit=75',
            ]
links_data_list = []

# #Function to get links of pages where you can find links to the offers
# def get_next_page_with_links():
#     # Get page links where you can find offer links
#     url = 'https://www.travelplanet.pl/wczasy/oferty/?kierunek=14:&wylot=26.04.2019&przylot=30.09.2019&osoby=2&dojazd=F&dzieci=2&wyzywienie=1&czas=6:8'
#     for i in range(3):
#         response = requests.get(url)
#         content = response.text
#         selector = Selector(text=content)
#
#         # Get next page url
#         # next_page_url = selector.css('.btn-pagination ~ a::attr(href)').get()
#         # next_page_url = selector.css(('a::attr(href)'))
#         next_page_url = selector.css(('#pagination--top > a:nth-child(7)::attr(href)'))
#         next_page_url = selector.css('#pagination--top > a:nth-child(7)')
#         print(next_page_url)
#         url_list.append(next_page_url)
#         url = next_page_url
#
# # Get page links where you can find offer links
# get_next_page_with_links()

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