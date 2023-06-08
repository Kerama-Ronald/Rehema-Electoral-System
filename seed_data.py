from sqlalchemy.orm import sessionmaker
from database import Base, Contestant, Category, Grade, Fee


##Session = sessionmaker(bind=engine)
##session = Session()

def seed_data():
    
    Base.metadata.create_all(engine)

    
    category1 = Category(School_level='Primary', Form_level='Upper Primary', Class_level='Class 7')
    category2 = Category(School_level='Secondary', Form_level='High School', Class_level='Form 3')

    grade1 = Grade(Student_Grade='B')
    grade2 = Grade(Student_Grade='C')

    fee1 = Fee(Fees_paid=0)
    fee2 = Fee(Fees_paid=100)

    contestant1 = Contestant(First_Name='Faith', Last_Name='Kilonzi', Gender='Male', Category=category1, Form='7A', Stream='S', Grade=grade1, Fees=fee1)
    contestant2 = Contestant(First_Name='Raphael', Last_Name='Katana', Gender='Female', Category=category2, Form='3B', Stream='T', Grade=grade2, Fees=fee2)

    ##session.add_all([category1, category2, grade1, grade2, fee1, fee2, contestant1, contestant2])
    ##session.commit()
