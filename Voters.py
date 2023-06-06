from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
