from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True)
    School_level = Column(String(32))
    Form_level = Column(String(32))
    Class_level = Column(String(32))

class Contestant(Base):
    __tablename__ = 'Contestants'
    id = Column(Integer, primary_key=True)
    First_Name = Column(String(32))
    Last_Name = Column(String(32))
    Gender = Column(String(32))
    Category_id = Column(Integer, ForeignKey('Categories.id'))
    Form = Column(String(32))
    Stream = Column(String(32))
    Grade_id = Column(Integer, ForeignKey('Grades.id'))
    Fees_id = Column(Integer, ForeignKey('Fees.id'))
    fees = relationship("Fees", foreign_keys=[Fees_id])

class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True)
    Student_Grade = Column(String(1))

class Fees(Base):
    __tablename__ = 'Fees'
    id = Column(Integer, primary_key=True)
    Balance = Column(Integer)

class Result(Base):
    __tablename__ = 'Results'
    id = Column(Integer, primary_key=True)
    Votes_garnered = Column(String(32))
    Votes_cast = Column(String(32))
    Percentage_votes = Column(Integer)
    contestant_id = Column(Integer, ForeignKey('Contestants.id'), unique=True)
    contestant = relationship("Contestant", backref="results")

class Voter(Base):
    __tablename__ = 'Voters'
    id = Column(Integer, primary_key=True)
    First_Name = Column(String(32))
    Last_Name = Column(String(32))
    Gender = Column(String(32))
    Form = Column(String(32))
    Stream = Column(String(32))
    results_id = Column(Integer, ForeignKey('Results.id'))
    results = relationship("Result", backref="voter")
