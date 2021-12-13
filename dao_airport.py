import os
import traceback
import jaydebeapi

my_sql_pass = os.environ.get("MYSQL_PASS")

def input_from_user():
    print("Select number: ")
    answer = int(input())
    return answer

def connect():
    con_try = None
    try:
        con_try = jaydebeapi.connect("com.mysql.cj.jdbc.Driver", "jdbc:MySQL://localhost/utopia",
                                     ["root", my_sql_pass], "C:/jars/mysql-connector-java-8.0.25/mysql-connector-java-8.0.25.jar")
        con_try.jconn.setAutoCommit(False)
    except jaydebeapi.Error:
        traceback.print_exc()
        print("There was a problem connecting to the database, please make sure the database information is correct!")
    except Exception:
        traceback.print_exc()
        print("General exception caught!")
    return con_try

def read_all_airports():
    conn = connect()
    cursor = conn.cursor()
    read_airports = "SELECT * FROM utopia.airport;"
    cursor.execute(read_airports)
    airports = cursor.fetchall()
    x = 1
    for airport in airports:
        print(str(x) + ": " + airport[0] + " " + airport[1])
        x = x + 1
    conn.commit()
    conn.close()
    return airports

def delete_airports():
    conn = connect()
    cursor = conn.cursor()
    print("Select the airport you want to delete.")
    d_list = read_all_airports()
    delete_specific_airport = input_from_user()
    iata_code = d_list[delete_specific_airport - 1]
    value = "\"" + iata_code[0] + "\""
    print(value)
    query = "delete from airport where iata_id = " + value
    cursor.execute(query)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #read_all_airports()
    delete_airports()


