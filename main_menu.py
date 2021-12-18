from utopia_airlines.MENUS import admin_menu


def show_welcome_message():
    print("\nWelcome to the Utopia Airlines Management System. Which category of a user are you?")


def user_category_options():
    print("1: Employee/Agent")
    print("2: Administrator")
    print("3: Traveler")


def int_from_user():
    while True:
        print("Select number: ")
        try:
            answer = int(input())
        except Exception:
            print("Invalid input. Please try again.")
            continue
        return answer

def input_from_user():
    user_answer = input()
    return user_answer


if __name__ == '__main__':
    while True:
        show_welcome_message()
        user_category_options()
        response = int_from_user()
        if response == 2:
            admin_menu.a_menu()
            continue
        print("Invalid selection. Please try again.")
