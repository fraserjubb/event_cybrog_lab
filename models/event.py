class Event:
    def __init__(self, date, name, number_of_guests, location, description, recurring):
        self.date = date
        self.name = name
        self.number_of_guests = number_of_guests
        self.location = location
        self.description = description
        self.recurring = recurring