import dao_airport

def input_from_user():
    print("Select number: ")
    answer = int(input())
    return answer

def flights_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    flights_options_response = input_from_user()
    print(flights_options_response)


def seats_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    seats_options_response = input_from_user()
    print(seats_options_response)


def tickets_and_passengers_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    tickets_and_passengers_options_response = input_from_user()
    print(tickets_and_passengers_options_response)


def airports_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    airports_options_response = input_from_user()
    if airports_options_response == 3:
        dao_airport.delete_airports()
    if airports_options_response == 4:
        dao_airport.read_all_airports()


def travelers_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    travelers_options_response = input_from_user()
    print(travelers_options_response)


def employees_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    employees_options_response = input_from_user()
    print(employees_options_response)

def override_options_menu():
    print("Please select from one of the four options:\n")
    print("1) Add")
    print("2) Update")
    print("3) Delete")
    print("4) Read")
    override_options_response = input_from_user()
    print(override_options_response)