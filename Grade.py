from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True)
    Student_Grade = Column(String(1))
