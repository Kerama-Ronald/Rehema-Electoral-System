from database import Category, Contestant, Result, session
from seed_data import seed_data

def show_menu():
    print("\nWelcome to Rehema Election System!")
    print("1. View Contestants")
    print("2. View Categories")
    print("3. View Winners")
    print("4. Vote")
    print("5. Seed Data (Developer mode)")
    print("6. Exit")

def handle_menu_choice(choice):
    if choice == 1:
        view_contestants()
    elif choice == 2:
        view_categories()
    elif choice == 3:
        view_winners()
    elif choice == 4:
        vote()
    elif choice == 5:
        seed_data()
    elif choice == 6:
        exit_program()
    else:
        print("Invalid choice. Please try again.")

def view_contestants():
    contestants = session.query(Contestant).all()
    for index, contestant in enumerate(contestants, start=1):
        print(f"{index}. ID: {contestant.id}, Name: {contestant.First_Name} {contestant.Last_Name}")

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

def vote():
    view_contestants()
    contestant_choice = int(input("Enter the number of the contestant you want to vote for: "))
    contestants = session.query(Contestant).all()
    if 1 <= contestant_choice <= len(contestants):
        contestant_id = contestants[contestant_choice - 1].id
        result = Result(Votes_garnered="1", Votes_cast="1", Percentage_votes=100, contestant_id=contestant_id)
        session.add(result)
        session.commit()
        print("Vote cast successfully!")
    else:
        print("Invalid contestant choice!")
