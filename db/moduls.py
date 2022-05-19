import os
import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, DATE, LargeBinary, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_str = 'sqlite:///' + \
                 os.path.join(
                     BASE_DIR, 'magasindata.db?check_same_thread=False')
engine = create_engine(connection_str)
base = declarative_base()


class Magsin(base):
    __tablename__ = "magsin"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    dato_Id = Column(DATE(), default=datetime.date.today(), nullable=False)
    iso_uke = Column(Integer, nullable=False)
    fyllingsgrad = Column(Integer, nullable=False)
    kapasitet_TWh = Column(Integer, nullable=False)
    fylling_TWh = Column(Integer, nullable=False)
    fyllingsgrad_forrige_uke = Column(Integer, nullable=False)
    endring_fyllingsgrad = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.dato_Id} - {self.iso_uke} - {self.fyllingsgrad} - {self.kapasitet_TWh} - {self.fylling_TWh} - {self.fyllingsgrad_forrige_uke} - {self.endring_fyllingsgrad}"


base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)
