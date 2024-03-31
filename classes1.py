class Flight():
    def __init__(self, capacity):   
        self.capacity = capacity
        self.passengers = []
    
    # add passenger method
    def add_passenger(self, name):
        self.passengers.append(name)
    
        # we can't keep adding passengers to the flight without known the capacity of the plane, like taking into consideration, if there is any open seat available. We have to create a new function to determine that for us
        # open seats method
    def open_seats(self):
        return self.capacity - self.passengers

flight = Flight(3)
