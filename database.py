from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///rehema.db')
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True)
    School_level = Column(String(32))
    Form_level = Column(String(32))
    Class_level = Column(String(32))
    contestants = relationship("Contestant", backref="category")

class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True)
    Grade_name = Column(String(32))
    contestants = relationship("Contestant", backref="grade")

class Fee(Base):
    __tablename__ = 'Fees'
    id = Column(Integer, primary_key=True)
    Amount = Column(Integer)
    contestants = relationship("Contestant", backref="fee")

class Contestant(Base):
    __tablename__ = 'Contestants'
    id = Column(Integer, primary_key=True)
    First_Name = Column(String(32))
    Last_Name = Column(String(32))
    Gender = Column(String(32))
    Category_id = Column(Integer, ForeignKey('Categories.id'))
    Form = Column(String(32))
    Stream = Column(String(32))
    Grade_id = Column(Integer, ForeignKey('Grades.id'))
    Fees_id = Column(Integer, ForeignKey('Fees.id'))

def create_category():
    school_level = input("Enter School Level: ")
    form_level = input("Enter Form Level: ")
    class_level = input("Enter Class Level: ")
    category = Category(School_level=school_level, Form_level=form_level, Class_level=class_level)
    session.add(category)
    session.commit()
    print("Category created successfully!")

def create_grade():
    grade_name = input("Enter Grade Name: ")
    grade = Grade(Grade_name=grade_name)
    session.add(grade)
    session.commit()
    print("Grade created successfully!")

def create_fee():
    amount = int(input("Enter Fee Amount: "))
    fee = Fee(Amount=amount)
    session.add(fee)
    session.commit()
    print("Fee created successfully!")

def create_contestant():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    gender = input("Enter Gender: ")
    category_id = int(input("Enter Category ID: "))
    form = input("Enter Form: ")
    stream = input("Enter Stream: ")
    grade_id = int(input("Enter Grade ID: "))
    fees_id = int(input("Enter Fees ID: "))
    contestant = Contestant(First_Name=first_name, Last_Name=last_name, Gender=gender, Category_id=category_id,
                            Form=form, Stream=stream, Grade_id=grade_id, Fees_id=fees_id)
    session.add(contestant)
    session.commit()
    print("Contestant created successfully!")

def read_categories():
    categories = session.query(Category).all()
    print("Categories:")
    for category in categories:
        print(f"ID: {category.id}, School Level: {category.School_level}, Form Level: {category.Form_level}, "
              f"Class Level: {category.Class_level}")

def read_grades():
    grades = session.query(Grade).all()
    print("Grades:")
    for grade in grades:
        print(f"ID: {grade.id}, Grade Name: {grade.Grade_name}")

def read_fees():
    fees = session.query(Fee).all()
    print("Fees:")
    for fee in fees:
        print(f"ID: {fee.id}, Amount: {fee.Amount}")

def read_contestants():
    contestants = session.query(Contestant).all()
    print("Contestants:")
    for contestant in contestants:
        print(f"ID: {contestant.id}, First Name: {contestant.First_Name}, Last Name: {contestant.Last_Name}, "
              f"Gender: {contestant.Gender}, Category ID: {contestant.Category_id}, Form: {contestant.Form}, "
              f"Stream: {contestant.Stream}, Grade ID: {contestant.Grade_id}, Fees ID: {contestant.Fees_id}")

def update_category():
    category_id = int(input("Enter Category ID to update: "))
    category = session.query(Category).get(category_id)
    if category:
        school_level = input("Enter School Level: ")
        form_level = input("Enter Form Level: ")
        class_level = input("Enter Class Level: ")
        category.School_level = school_level
        category.Form_level = form_level
        category.Class_level = class_level
        session.commit()
        print("Category updated successfully!")
    else:
        print("Category not found!")

def update_grade():
    grade_id = int(input("Enter Grade ID to update: "))
    grade = session.query(Grade).get(grade_id)
    if grade:
        grade_name = input("Enter Grade Name: ")
        grade.Grade_name = grade_name
        session.commit()
        print("Grade updated successfully!")
    else:
        print("Grade not found!")

def update_fee():
    fee_id = int(input("Enter Fee ID to update: "))
    fee = session.query(Fee).get(fee_id)
    if fee:
        amount = int(input("Enter Fee Amount: "))
        fee.Amount = amount
        session.commit()
        print("Fee updated successfully!")
    else:
        print("Fee not found!")

def update_contestant():
    contestant_id = int(input("Enter Contestant ID to update: "))
    contestant = session.query(Contestant).get(contestant_id)
    if contestant:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        category_id = int(input("Enter Category ID: "))
        form = input("Enter Form: ")
        stream = input("Enter Stream: ")
        grade_id = int(input("Enter Grade ID: "))
        fees_id = int(input("Enter Fees ID: "))
        contestant.First_Name = first_name
        contestant.Last_Name = last_name
        contestant.Gender = gender
        contestant.Category_id = category_id
        contestant.Form = form
        contestant.Stream = stream
        contestant.Grade_id = grade_id
        contestant.Fees_id = fees_id
        session.commit()
        print("Contestant updated successfully!")
    else:
        print("Contestant not found!")

def delete_category():
    category_id = int(input("Enter Category ID to delete: "))
    category = session.query(Category).get(category_id)
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted successfully!")
    else:
        print("Category not found!")

def delete_grade():
    grade_id = int(input("Enter Grade ID to delete: "))
    grade = session.query(Grade).get(grade_id)
    if grade:
        session.delete(grade)
        session.commit()
        print("Grade deleted successfully!")
    else:
        print("Grade not found!")

def delete_fee():
    fee_id = int(input("Enter Fee ID to delete: "))
    fee = session.query(Fee).get(fee_id)
    if fee:
        session.delete(fee)
        session.commit()
        print("Fee deleted successfully!")
    else:
        print("Fee not found!")

def delete_contestant():
    contestant_id = int(input("Enter Contestant ID to delete: "))
    contestant = session.query(Contestant).get(contestant_id)
    if contestant:
        session.delete(contestant)
        session.commit()
        print("Contestant deleted successfully!")
    else:
        print("Contestant not found!")

def main_menu():
    while True:
        print("\n--- Rehema Electoral System ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_menu()
        elif choice == '2':
            read_menu()
        elif choice == '3':
            update_menu()
        elif choice == '4':
            delete_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def create_menu():
    while True:
        print("\n--- Create Menu ---")
        print("1. Create Category")
        print("2. Create Grade")
        print("3. Create Fee")
        print("4. Create Contestant")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_category()
        elif choice == '2':
            create_grade()
        elif choice == '3':
            create_fee()
        elif choice == '4':
            create_contestant()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def read_menu():
    while True:
        print("\n--- Read Menu ---")
        print("1. Read Categories")
        print("2. Read Grades")
        print("3. Read Fees")
        print("4. Read Contestants")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            read_categories()
        elif choice == '2':
            read_grades()
        elif choice == '3':
            read_fees()
        elif choice == '4':
            read_contestants()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def update_menu():
    while True:
        print("\n--- Update Menu ---")
        print("1. Update Category")
        print("2. Update Grade")
        print("3. Update Fee")
        print("4. Update Contestant")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            update_category()
        elif choice == '2':
            update_grade()
        elif choice == '3':
            update_fee()
        elif choice == '4':
            update_contestant()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def delete_menu():
    while True:
        print("\n--- Delete Menu ---")
        print("1. Delete Category")
        print("2. Delete Grade")
        print("3. Delete Fee")
        print("4. Delete Contestant")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            delete_category()
        elif choice == '2':
            delete_grade()
        elif choice == '3':
            delete_fee()
        elif choice == '4':
            delete_contestant()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main_menu()
