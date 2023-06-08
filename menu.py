from unittest import result
from flask import sessions
from database import Category, Contestant, Result, session
from seed_data import seed_data


def show_menu():
    print("\nWelcome to Rehema Election System!")
    print("1. View Contestants")
    print("2. View Categories")
    print("3. View Winners")
    print("4. Seed Data (Developer mode)")
    print("5. Exit")

def handle_menu_choice(choice):
    if choice == 1:
        view_contestants()
    elif choice == 2:
        view_categories()
    elif choice == 3:
        view_winners()
    elif choice == 4:
        seed_data()
    elif choice == 5:
        exit_program()
    else:
        print("Invalid choice. Please try again.")

def view_contestants():
    contestants = session.query(Contestant).all()
    for contestant in contestants:
        print(f"ID: {contestant.id}, Name: {contestant.First_Name} {contestant.Last_Name}")

def view_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(f"ID: {category.id}, Level: {category.School_level}, Form Level: {category.Form_level}")

def view_winners():
    winners = session.query(Contestant).join(Result).filter(Result.Percentage_votes == 100).all()
    for winner in winners:
        print(f"ID: {winner.id}, Name: {winner.First_Name} {winner.Last_Name}")

def exit_program():
    session.close()
    print("Thank you for using the Election System. Goodbye!")
    exit(0)