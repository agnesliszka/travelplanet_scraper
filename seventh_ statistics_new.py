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
    keyword = input("Input next keyword to be added to the list: ")
    keywords.append(keyword)
    print("The current list of keywords: " + str(keywords))
    print("To input next keyword select 1 ")

# my_key_words = ['brodzik', 'piaszczysta plaza', 'plac zabaw', 'menu dla dzieci', 'animacje dla dzieci']

# Define a query map
QUERY_MAP = {
    'number_of_offers': 'SELECT COUNT (*) FROM oferty_wakacyjne WHERE tresc_oferty LIKE keywords[0] AND tresc_oferty LIKE keywords[1] AND tresc_oferty LIKE keywords[2] AND tresc_oferty LIKE keywords[3] AND tresc_oferty LIKE keywords[4];',
    'offers_links': 'SELECT html FROM oferty_wakacyjne WHERE tresc_oferty LIKE keywords[0] AND tresc_oferty LIKE keywords[1] AND tresc_oferty LIKE keywords[2] AND tresc_oferty LIKE keywords[3] AND tresc_oferty LIKE keywords[4];',
    }

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

def offers_data():
    print(keywords)
    number_of_offers = run_query(QUERY_MAP['number_of_offers'], path_to_db)
    offers_links = run_query(QUERY_MAP['offers_links'], path_to_db)
    print('number of offers: ' + str(number_of_offers[0][0]))
    print('offers links: ')
    for link in offers_links:
        print(link[0])

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        Choose one of the following options         
        1 - add keyword to the list of keywords to be searched in offers
        2 - show selected offers links
        3 - close 
        ''')
        if user_choice == "1":
            if len(keywords)<5:
                add_keyword()
            else:
                print("You have already inputted 5 keywords")
        elif user_choice == "2":
            offers_data()
        elif user_choice == "3":
            return
        else:
            print("Choose the correct option: 1, 2 or 3.")
    return

# Run menu
menu()

