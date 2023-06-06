from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fee(Base):
    __tablename__ = 'Fees'
    id = Column(Integer, primary_key=True)
    Fees_paid = Column(Integer)
    contestant_id = Column(Integer, ForeignKey('Contestants.id'), unique=True)
