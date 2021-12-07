import admin_menu


def welcome_message():
    print("Welcome to the Utopia Airlines Management System. Which category of a user are you?")


def user_category_options():
    print("1: Employee/Agent")
    print("2: Administrator")
    print("3: Traveler")


def input_from_user():
    print("Select number: ")
    answer = int(input())
    return answer


if __name__ == '__main__':
    welcome_message()
    user_category_options()
    response = input_from_user()
    if response == 2:
        admin_menu.a_menu()
