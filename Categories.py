from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True)
    School_level = Column(String(32))
    Form_level = Column(String(32))
    Class_level = Column(String(32))

    