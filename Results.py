from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Result(Base):
    __tablename__ = 'Results'
    id = Column(Integer, primary_key=True)
    Votes_garnered = Column(String(32))
    Votes_cast = Column(String(32))
    Percentage_votes = Column(Integer)
    contestant_id = Column(Integer, ForeignKey('Contestants.id'), unique=True)
    contestant = relationship("Contestant", backref="results")
