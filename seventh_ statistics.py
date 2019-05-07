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

# Define a query map
QUERY_MAP = {
    'ilosc_ofert': 'SELECT COUNT (*) FROM oferty_wakacyjne WHERE tresc_oferty LIKE "%piaszczyst%" AND tresc_oferty LIKE "%plaza%" AND tresc_oferty LIKE "%brodzik%";',
    'dane_ofert': 'SELECT html FROM oferty_wakacyjne WHERE tresc_oferty LIKE "%piaszczyst%" AND tresc_oferty LIKE "%plaza%" AND tresc_oferty LIKE "%brodzik%";',
    }

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

ilosc_ofert = run_query(QUERY_MAP['ilosc_ofert'], path_to_db)

def dane_ofert():
    ilosc_ofert = run_query(QUERY_MAP['ilosc_ofert'], path_to_db)
    dane_ofert = run_query(QUERY_MAP['dane_ofert'], path_to_db)
    print('ilosc_ofert: ' + str(ilosc_ofert))
    print('dane_ofert: ' + str(dane_ofert))

# Key words:
slowa_klucz = ['brodzik', 'piaszczysta plaza', 'plac zabaw', 'kacik dla dzieci', 'menu dla dzieci', 'animacje dla dzieci']

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        Wybierz jedna z ponizszych opcji:         
        1 - pokaz dane ofert 
        2 - zakoncz program
        ''')
        if user_choice == "1":
            dane_ofert()
        elif user_choice == "2":
            return
        else:
            print("Wybierz jeszcze raz odpowiedni numer opcji.")
    return

# Run menu
menu()

