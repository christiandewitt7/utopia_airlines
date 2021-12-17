from utopia_airlines.DAO import dao_airport
from utopia_airlines.main_menu import int_from_user


def flights_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    flights_options_response = int_from_user()
    print(flights_options_response)


def seats_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    seats_options_response = int_from_user()
    print(seats_options_response)


def tickets_and_passengers_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    tickets_and_passengers_options_response = int_from_user()
    print(tickets_and_passengers_options_response)


def airports_options_menu():
    while True:
        print("\nPlease select from one of the four options:\n")
        print("1) Add Airports")
        print("2) Update Airports")
        print("3) Delete Airports")
        print("4) Read Airports")
        airports_options_response = int_from_user()
        if airports_options_response == 1:
            dao_airport.add_airports()
        elif airports_options_response == 3:
            dao_airport.delete_airports()
        elif airports_options_response == 4:
            dao_airport.read_all_airports()
        else:
            print("Invalid input. Please try again.")
            continue
        print("\nWould you like to try another airport operation? Y/N")
        airports_again = input()
        if airports_again.upper() == "Y":
            continue
        else:
            break


def travelers_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    travelers_options_response = int_from_user()
    print(travelers_options_response)


def employees_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    employees_options_response = int_from_user()
    print(employees_options_response)

def override_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    override_options_response = int_from_user()
    print(override_options_response)