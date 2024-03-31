class Flight():
    def __init__(self, capacity):   
        self.capacity = capacity
        self.passengers = []
    
    # add passenger method
    def add_passenger(self, name):
        self.passengers.append(name)

flight = Flight(3)
