# 3rd party imports
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# Create 'vacation offers' database schema
class Offer(Base):
    # Set a table name
    __tablename__ = 'oferty_wakacyjne'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    id_oferty = Column(String)
    lokalizacja = Column(String, nullable='True')
    tytul = Column(String, nullable='True')
    cena_za_osobe = Column(String, nullable='True')
    cena_za_calosc = Column(String, nullable='True')
    html = Column(String, nullable='True')
    tresc_oferty = Column(String, nullable='True')
