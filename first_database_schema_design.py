# 3rd party imports
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


# Create 'offers' database schema
class Offer(Base):
    # Set a table name
    __tablename__ = 'vacation_offers'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    # id_oferty = Column(String)
    lokalizacja = Column(String, nullable='True')
    tytul = Column(String, nullable='True')
    # cena = Column(String, nullable='True')
    html = Column(String, nullable='True')
    text = Column(String, nullable='True')

