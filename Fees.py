from sqlalchemy import create_engine,Column,String,Integer,Base
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

class Contestants(Base):
    __tablename__ = 'Contestants'
    id=Column(Integer, primary_key=True)
    Fees_paid=Column(Integer)
    