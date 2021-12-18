import os  # operating system....so that my password doesnt have to show
import traceback # error tracing library that prints out errors to your command line.
import jaydebeapi  # some sort of SQL connector

#from utopia_airlines.main_menu import int_from_user, input_from_user
from utopia_airlines.models.airports import Airports

my_sql_pass = os.environ.get("MYSQL_PASS")


def connect():
    con_try = None
    try:
        con_try = jaydebeapi.connect("com.mysql.cj.jdbc.Driver", "jdbc:MySQL://localhost/utopia",
                                     ["root", my_sql_pass],
                                     "C:/jars/mysql-connector-java-8.0.25/mysql-connector-java-8.0.25.jar")
        con_try.jconn.setAutoCommit(False)
    except jaydebeapi.Error:  # catch jaydebeapi exception
        traceback.print_exc()
        print("There was a problem connecting to the database, please make sure the database information is correct!")
    except Exception:  # catch all exceptions
        traceback.print_exc()
        print("General exception caught!")
    return con_try


def read_all_airports():
    conn = connect()   # connecting the database
    cursor = conn.cursor() # cursor is the SQL tool
    read_airports = "SELECT * FROM utopia.airport;"  # SQL query to select all airports
    cursor.execute(read_airports) # runs the SQL query
    airports_sql_data_tuple = cursor.fetchall() # look up cursor statements
    menu_number = 1
    all_airports = []
    for airport_data in airports_sql_data_tuple: #printing out the menu and also returning the list of all airport objects so we can use it elsewhere
        current_iata_id = airport_data[0]
        current_city = airport_data[1]
        current_airport = Airports(current_iata_id, current_city)
        current_airport.print_airport(menu_number)
        #print(str(menu_number) + ": " + current_airport.iata_id + " " + current_airport.city)
        menu_number = menu_number + 1
        all_airports.append(current_airport)
    conn.commit()
    conn.close()
    return all_airports  # gives the info i want and ends the function.


def delete_airports():
    conn = connect()
    cursor = conn.cursor()
    print("Select the airport you want to delete.")
    d_list = read_all_airports()  # the list we want from this particular function, also printing out menu.
    d_object = d_list[int_from_user() - 1] # set d_object to a singular airport that the user selected.
    print(d_object)
    value = "\"" + (d_object.iata_id) + "\""
    query = "delete from airport where iata_id = " + value
    cursor.execute(query)
    conn.commit()
    conn.close()

def add_airports():
    conn = connect()
    cursor = conn.cursor()
    print("Input the airport code you want to add.")
    airport_code = input_from_user()
    print("Input the city name you want to add.")
    city_code = input_from_user()
    # put this in a separate function >>>>if i type a duplicate entry there is currently no way to catch it...select statement from mySQL where iata_id == to airport_code...., put that object into a tuple (reference read_airports) if iata_code exists, function should just return.
    add_airports_user = "insert into airport(iata_id, city) Values(\"" + airport_code + "\", \"" + city_code + "\");"
    cursor.execute(add_airports_user)
    conn.commit()
    conn.close()
    return add_airports_user
    #insert into airport(iata_id, city) Values("PIT", "Pittsburgh");

def input_from_user():
    user_answer = input()
    return user_answer

def int_from_user():
    while True:
        print("Select number: ")
        try:
            answer = int(input())
        except Exception:
            print("Invalid input. Please try again.")
            continue
        return answer


if __name__ == '__main__':
    # read_all_airports()
    #delete_airports()
    #a1 = Airports("BWI", "Baltimore")
    # print(a1.iata_id)
    # a1.print_airport()
    print(add_airports())
