passengers = []
class Humans():
    def __init__(self, name):
        self.name = name

class Passengers(Humans):
    class_variable = []
    def __init__(self, name, passnum):
        self.name = name
        self.passnum = passnum
        Passengers.class_variable.append(self)

class Staff(Humans):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

class Aircraft():
    def __init__(self, name):
        self.name = name

class Planes(Aircraft):
    def __init__(self, name, planenum):
        self.name = name
        self.planenum = planenum

class Flight():
    class_variable = []
    def __init__(self, name = 'None', origin = 'None', destination = 'None', planenum = 0):
        self.name = name
        self.planenum = planenum
        self.origin = origin
        self.destination = destination
        Flight.class_variable.append(self)
    def add_passengers(self, Passengers):
        passengers.append(Passengers)
    def add_origin(self, origin):
        self.origin = origin
    def add_destination(self, destination):
        self.destination = destination
    def add_plane(self, name):
        self.name = name



