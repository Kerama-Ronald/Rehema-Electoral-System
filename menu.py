from ctypes import HRESULT
from unittest import result
from flask import sessions
from database import Category, Contestant, Session


def show_menu():
    print("Welcome to the Election System!")
    print("1. View Contestants")
    print("2. View Categories")
    print("3. View Winners")
    print("4. Exit")

def handle_menu_choice(choice):
    if choice == 1:
        view_contestants()
    elif choice == 2:
        view_categories()
    elif choice == 3:
        view_winners()
    elif choice == 4:
        exit_program()
    else:
        print("Invalid choice. Please try again.")

def view_contestants():
    contestants = Session.query(Contestant).all()
    for contestant in contestants:
        print(f"ID: {contestant.id}, Name: {contestant.First_Name} {contestant.Last_Name}")

def view_categories():
    categories = sessions.query(Category).all()
    for category in categories:
        print(f"ID: {category.id}, Level: {category.School_level}, Form Level: {category.Form_level}")

def view_winners():
    winners = Session.query(Contestant).join(HRESULT).filter(result.Percentage_votes == 100).all()
    for winner in winners:
        print(f"ID: {winner.id}, Name: {winner.First_Name} {winner.Last_Name}")

def exit_program():
    Session.close()
    print("Thank you for using the Election System. Goodbye!")

def main():
    show_menu()
    choice = int(input("Enter your choice: "))
    handle_menu_choice(choice)

if __name__ == '__main__':
    main()

