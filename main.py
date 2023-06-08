from menu import handle_menu_choice, show_menu

if __name__ == '__main__':
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            handle_menu_choice(choice)
        except ValueError:
            print("Invalid choice. Please try again.")