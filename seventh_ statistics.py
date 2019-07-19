# Standard library imports
import os
import sqlite3

# 3rd party imports
from sqlalchemy.sql import func

# Project imports
from first_database_schema_design import Offer
from second_db_engine import Session


session = Session()

# Function to run a database query
def run_query(query, db):
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result

# Keywords:
keywords = []

def add_keyword():
    first_keyword = input("Input first keyword to be added to the list: ")
    keywords.append(first_keyword)
    second_keyword = input("Input second keyword to be added to the list: ")
    keywords.append(second_keyword)
    third_keyword = input("Input third keyword to be added to the list: ")
    keywords.append(third_keyword)
    print("The current list of keywords: " + str(keywords))
    print("To input next keyword select 1 ")

# my_key_words = ['brodzik', 'piaszczysta plaza', 'plac zabaw', 'menu dla dzieci', 'animacje dla dzieci']

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

def offers_data():
    print(keywords)

    QUERY_MAP = {
        'number_of_offers': 'SELECT COUNT (*) FROM oferty_wakacyjne WHERE tresc_oferty LIKE "%{first}%" AND tresc_oferty LIKE "%{second}%" AND tresc_oferty LIKE "%{third}%";'.format(first=keywords[0], second=keywords[1], third=keywords[2]),
        'offers_links': 'SELECT html FROM oferty_wakacyjne WHERE tresc_oferty LIKE "%{first}%" AND tresc_oferty LIKE "%{second}%" AND tresc_oferty LIKE "%{third}%";'.format(first=keywords[0], second=keywords[1], third=keywords[2]),
    }

    number_of_offers = run_query(QUERY_MAP['number_of_offers'], path_to_db)
    offers_links = run_query(QUERY_MAP['offers_links'], path_to_db)
    print('number of offers: ' + str(number_of_offers[0][0]))
    print('offers links: ')
    for link in offers_links:
        print(link[0])

# Create a menu representing available options
def menu():
    users_input=input('''The program allows you to input three keywords that you want to find in the offers page.
If you want to add a keyword press any key (except 'c'). To close the program input 'c' 
''')
    if users_input=="c":
        return
    else:
        add_keyword()
        offers_data()
    return

# Run menu
menu()

