from sqlalchemy import engine_from_config
from database import Base, create_category, create_contestant, create_fee, create_grade, delete_category, delete_contestant, delete_fee, delete_grade, read_categories, read_fees, read_grades, update_category, update_contestant, update_fee, update_grade
from queries import get_contestants


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
            get_contestants()
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
    Base.metadata.create_all(engine_from_config)
    main_menu()
