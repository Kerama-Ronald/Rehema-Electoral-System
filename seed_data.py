from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Contestant, Category, Fee, Grade

engine = create_engine("sqlite:///rehema.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    category1 = Category(School_level='Primary', Form_level='Upper Primary', Class_level='Class 7')
    category2 = Category(School_level='Secondary', Form_level='High School', Class_level='Form 3')

    grade1 = Grade(Student_Grade='B')
    grade2 = Grade(Student_Grade='C')

    fee1 = Fee(Amount=0)
    fee2 = Fee(Amount=100)

    contestant1 = Contestant(First_Name='Faith', Last_Name='Kilonzi', Gender='Male', Form='7A', Stream='S')
    contestant2 = Contestant(First_Name='Raphael', Last_Name='Katana', Gender='Female', Form='3B', Stream='T')

    session.add_all([category1, category2, fee1, fee2, grade1, grade2, contestant1, contestant2])
    session.commit()

seed_data()