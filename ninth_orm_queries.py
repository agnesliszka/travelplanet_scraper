# Standard library imports
from sqlalchemy import and_

# Project imports
from second_db_engine import Session
from first_database_schema_design import Offer


session = Session()

results = session.query(Offer).filter(and_(Offer.tresc_oferty.ilike('%brodzik%')).all()
# print(results)
#, Offer.tresc_oferty.ilike('%dla dzieci%'), Offer.tresc_oferty.ilike('%piaszczysta plaża%')