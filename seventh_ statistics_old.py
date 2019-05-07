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
    'ilosc_ofert': 'SELECT COUNT (*) FROM oferty_wakacyjne;',
    'dane_oferty': 'SELECT * FROM oferty_wakacyjne;',
    'id_oferty': 'SELECT id_oferty FROM oferty_wakacyjne;',
    'lokalizacja': 'SELECT lokalizacja FROM oferty_wakacyjne;',
    'tytul': 'SELECT tytul FROM oferty_wakacyjne;',
    'cena_za_osobe': 'SELECT cena_za_osobe FROM oferty_wakacyjne;',
    'cena_za_calosc': 'SELECT cena_za_calosc FROM oferty_wakacyjne;',
    'html': 'SELECT html FROM oferty_wakacyjne;',
    'tresc_oferty': 'SELECT tresc_oferty FROM oferty_wakacyjne;',
}

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

ilosc_ofert = run_query(QUERY_MAP['ilosc_ofert'], path_to_db)

# Function to get html of the offer
def html():
    html = run_query(QUERY_MAP['html'], path_to_db)
    print('html: ' + str(html))
    return html

# Function to get general statistics - number of offers
def general_info():
    # Get offer data from the database
    id_oferty = run_query(QUERY_MAP['id_oferty'], path_to_db)
    print('id_oferty: ' + str(id_oferty))
    lokalizacja = run_query(QUERY_MAP['lokalizacja'], path_to_db)
    print('lokalizacja: ' + str(lokalizacja))
    tytul = run_query(QUERY_MAP['tytul'], path_to_db)
    print('tytul: ' + str(tytul))
    cena_za_osobe = run_query(QUERY_MAP['cena_za_osobe'], path_to_db)
    print('cena_za_osobe: ' + str(cena_za_osobe))
    cena_za_calosc = run_query(QUERY_MAP['cena_za_calosc'], path_to_db)
    print('cena_za_calosc: ' + str(cena_za_calosc))
    return id_oferty, lokalizacja, tytul, cena_za_osobe, cena_za_calosc

# Key words:
slowa_klucz_nonpln = ['brodzik', 'piaszczysta plaza', 'plac zabaw', 'kacik dla dzieci', 'menu dla dzieci', 'animacje dla dzieci']
slowa_klucz_pln = ['brodzik', 'piaszczysta plaża', 'plac zabaw', 'kącik dla dzieci', 'menu dla dzieci', 'animacje dla dzieci']
dzieci = ['dla dzieci', 'idealne dla dzieci', 'dobre dla dzieci']
brodzik = ['brodzik', 'brodziki']
plaza = ['piaszczysta plaza', 'piaszczysta plaża']
kacik_dla_dzieci = ['kacik dla dzieci', 'kącik dla dzieci']
plac_zabaw = ['plac zabaw']
menu = ['menu dla dzieci']
animacje = ['animacje dla dzieci']

def slowa_klucz_nonpln():
    if all(i in html for i in slowa_klucz_nonpln) == True:
        general_info()

def slowa_klucz_pln():
    if all(i in html for i in slowa_klucz_pln) == True:
        general_info()

def dla_dzieci():
    if any(i in html for i in dzieci) == True:
        general_info()

def brodzik():
    if any(i in html for i in brodzik) == True:
        general_info()

def plaza():
    if any(i in html for i in plaza) == True:
        general_info()

def kacik_dla_dzieci():
    if any(i in html for i in kacik_dla_dzieci) == True:
        general_info()

def plac_zabaw():
    if all(i in html for i in plac_zabaw) == True:
        general_info()

def menu():
    if all(i in html for i in menu) == True:
        general_info()

def animacje():
    if all(i in html for i in animacje) == True:
        general_info()

def slowa_klucz_nonpln_wynik():
    for i in range(ilosc_ofert): #jak sie iterowac po bazie danych
        html()
        slowa_klucz_nonpln()

def slowa_klucz_pln_wynik(): #jak sie iterowac po bazie danych
    for i in range(ilosc_ofert):
        html()
        slowa_klucz_pln()

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        Wybierz jedna z ponizszych opcji:         
        1 - pokaz dane ofert, ktore zawieraja wszystkie slowa kluczowe nonpln 
        2 - pokaz dane ofert, ktore zawieraja wszystkie slowa kluczowe pln
        3 - zakoncz program  
        ''')
        if user_choice == "1":
            slowa_klucz_nonpln_wynik()
        elif user_choice == "2":
            slowa_klucz_pln_wynik()
        elif user_choice == "3":
            return
        else:
            print("Wybierz jeszcze raz odpowiedni numer opcji.")
    return

# Run menu
menu()

