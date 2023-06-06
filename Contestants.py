from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    category = relationship("Category", backref="contestants")
    grade = relationship("Grade", backref="contestants")
    fees = relationship("Fee", uselist=False, backref="contestant")
    results = relationship("Result", uselist=False, backref="contestant")
