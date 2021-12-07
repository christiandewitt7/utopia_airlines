def a_menu():
    print("Please select your admin function:\n")
    print("1) Add / Update / Delete / Read: Flights")
    print("2) Add / Update / Delete / Read: Seats")
    print("3) Add / Update / Delete / Read: Tickets and Passengers")
    print("4) Add / Update / Delete / Read: Airports")
    print("5) Add / Update / Delete / Read: Travelers")
    print("6) Add / Update / Delete / Read: Employees")
    print("7) Over-ride Trip Cancellation for a ticket.")
    user_response = input_from_user()
    print(user_response)

def input_from_user():
    print("Select number: ")
    answer = int(input())
    return answer

