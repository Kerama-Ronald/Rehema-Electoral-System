from sqlalchemy import create_engine,Column,String,Integer,Base
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

class Contestants(Base):
    __tablename__ = 'Contestants'
    id=Column(Integer, primary_key=True)
    Votes_garnered=Column(String(32))
    Votes_cast=Column(String(32))
    Percentage_votes=Column(Integer)
    