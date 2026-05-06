from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import foreign

Base = declarative_base()

class Workers(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    ipn = Column(Integer)
    passport = Column(String)


class Child(Base):
    __tablename__ = 'childrens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    child_name = Column(String)
    birth_date = Column(DATE)
    parrent_ipn = Column(Integer, ForeignKey("workers.ipn"))


class Sallary(Base):
    __tablename__ = 'sallaries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ipn = Column(Integer, ForeignKey("workers.ipn"))
    month = Column(Integer)
    payment = Column(Integer)