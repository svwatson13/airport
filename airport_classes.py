class Humans():
    def __init__(self, name):
        self.name = name

class Passengers(Humans):
    def __init__(self, name, passnum):
        super().__init__(name)
        self.passnum = passnum




class Staff(Humans):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

class Aircraft():
    def __init__(self, name):
        self.name = name

class Planes(Aircraft):
    def __init__(self, name, planenum):
        super().__init__(name)
        self.planenum = planenum

    def plane(self):
        return self

    def planenum(self):
        return self


class Helicopter(Aircraft):
    def __init__(self):
        super().__init__(name)
        self.helinum = helinum

class Flight():
    def __init__(self, origin = 0, destination = 0, planenum = 0):
        self.planenum = planenum
        self.origin = origin
        self.destination = destination
    def list_of_passengers(self, passnum):
        self.passengers.append(passnum)

