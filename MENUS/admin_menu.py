from utopia_airlines.MENUS import all_options_menu


def a_menu():
    while True:
        print("Please select your admin function:\n")
        print("1) Add / Update / Delete / Read: Flights")
        print("2) Add / Update / Delete / Read: Seats")
        print("3) Add / Update / Delete / Read: Tickets and Passengers")
        print("4) Add / Update / Delete / Read: Airports")
        print("5) Add / Update / Delete / Read: Travelers")
        print("6) Add / Update / Delete / Read: Employees")
        print("7) Over-ride Trip Cancellation for a ticket.")
        user_response = all_options_menu.int_from_user()
        if user_response == 1:
            all_options_menu.flights_options_menu()
            break
        if user_response == 2:
            all_options_menu.seats_options_menu()
            break
        if user_response == 3:
            all_options_menu.tickets_and_passengers_options_menu()
            break
        if user_response == 4:
            all_options_menu.airports_options_menu()
            break
        if user_response == 5:
            all_options_menu.travelers_options_menu()
            break
        if user_response == 6:
            all_options_menu.employees_options_menu()
            break
        if user_response == 7:
            all_options_menu.override_options_menu()
            break
        print("\nInvalid selection. Please try again.")


