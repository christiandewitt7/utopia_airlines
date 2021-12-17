class Airports:
    def __init__(self, iata_id, city):
        self.iata_id = iata_id
        self.city = city

    def print_airport(self):
        print(str(self.iata_id) + " " + str(self.city))

