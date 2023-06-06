from sqlalchemy import create_engine,Column,String,Integer,Base
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

class Contestants(Base):
    __tablename__ = 'Contestants'
    id=Column(Integer, primary_key=True)
    First_Name=Column(String(32))
    Last_Name=Column(String(32))
    Gender=Column(String(32) )
    Form=Column(String(32))
    Stream=Column(String(32))
    Grade=Column(String(32))
    Fees_Balance=Column(Integer)