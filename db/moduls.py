import os
import datetime
from sqlalchemy import Column, Integer, create_engine, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_str = 'sqlite:///' + \
                 os.path.join(
                     BASE_DIR, 'magasindata.db?check_same_thread=False')
engine = create_engine(connection_str)
base = declarative_base()


class Magasin(base):
    __tablename__ = "magasin"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    dato_id = Column(DATE(), default=datetime.date.today(), nullable=False)
    iso_uke = Column(Integer, nullable=False)
    fyllingsgrad = Column(Integer, nullable=False)
    kapasitet_twh = Column(Integer, nullable=False)
    fylling_twh = Column(Integer, nullable=False)
    fyllingsgrad_forrige_uke = Column(Integer, nullable=False)
    endring_fyllingsgrad = Column(Integer, nullable=False)
    latitude = Column(Integer, nullable=False)
    longitude = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.dato_id} - {self.iso_uke} - {self.fyllingsgrad} - {self.kapasitet_twh} - {self.fylling_twh} - {self.fyllingsgrad_forrige_uke} - {self.endring_fyllingsgrad} - {self.latitude} - {self.longitude}"


base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)
