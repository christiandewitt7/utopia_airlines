class Airports:
    def __init__(self, iata_id, city):
        self.iata_id = iata_id
        self.city = city

    def print_airport(self, menu_item_number): # pass in the menu item so you can print out the airport in the proper format.
        print(str(menu_item_number) + ": " + (self.iata_id) + " " + str(self.city))

    #def get_routes(self):

    #this function is reading all routes associated with this instance of Airports. I can call this function after creating an Airports instance.
        # use self.iata_id to select * Routes whose origin_id's or whose destination_id == self.iata_id
        # save all the route id's to self.routes, alternatively maybe its better to just return them.
            # -if we have other functions in the Airports instance that could make use of self.routes then keep it on self. self (is the instance)
            # -if we just need the data to pass to other classes then maybe its better to just return the list of id's




# make add_route():
# 1. requires: id, origin id, destination id
# 2. create SQL entity in the routes table  with the given fields.