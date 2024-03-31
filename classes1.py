class Flight():
    def __init__(self, capacity):   
        self.capacity = capacity
        self.passengers = []
    
    # add passenger method
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
        # we can't keep adding passengers to the flight without known the capacity of the plane, like taking into consideration, if there is any open seat available. We have to create a new function to determine that for us
        # open seats method
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["John", "Esther", "Peter", "Mary"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")