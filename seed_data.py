from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Contestant, Category, Fee, Grade

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    category_1 = Category(School_level='Primary', Form_level='Form 1', Class_level='Class A')
    category_2 = Category(School_level='Primary', Form_level='Form 2', Class_level='Class B')
    category_3 = Category(School_level='Secondary', Form_level='Form 3', Class_level='Class C')

    session.add_all([category_1, category_2, category_3])
    session.commit()

    grade_1 = Grade(Student_Grade='A')
    grade_2 = Grade(Student_Grade='B')
    grade_3 = Grade(Student_Grade='C')
    session.add_all([grade_1, grade_2, grade_3])
    session.commit()

    fee_1 = Fee(Amount=100)
    fee_2 = Fee(Amount=150)
    fee_3 = Fee(Amount=200)
    session.add_all([fee_1, fee_2, fee_3])
    session.commit()

    contestant1 = Contestant(First_Name='Faith', Last_Name='Kilonzi', Gender='Male', Form='7A', Stream='S',  Category_id=3, Grade_id=3, Fees_id=3)
    contestant2 = Contestant(First_Name='Raphael', Last_Name='Katana', Gender='Female', Form='3B', Stream='T',  Category_id=3, Grade_id=3, Fees_id=3)
    contestant_3 = Contestant(First_Name='Bob', Last_Name='Johnson', Gender='Male', Form='Form 3', Stream='T', Category_id=3, Grade_id=3, Fees_id=3)
    session.add_all([contestant1, contestant2, contestant_3])
    session.commit()

if __name__ == '__main__':
    seed_data()
