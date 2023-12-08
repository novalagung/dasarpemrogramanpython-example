# %% A.39.1. Pengenalan Inheritance

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self):
        self.name = "common vehicle"
        self.number_of_wheels = 4
    
    def drive_sound(self):
        return "vroom vroooommmm"

class ElectricCar(Vehicle):
    def info(self):
        print(self.name, "has", self.number_of_wheels, "wheels. engine sound:", self.drive_sound())

v1 = Vehicle()
if isinstance(v1, Vehicle):
    print("v1 class inherit from class Vehicle")
if isinstance(v1, object):
    print("v1 class inherit from class object")

v2 = ElectricCar()
if isinstance(v2, ElectricCar):
    print("v2 class inherit from class ElectricCar")
if isinstance(v2, Vehicle):
    print("v2 class inherit from class Vehicle")
if isinstance(v2, object):
    print("v2 class inherit from class object")
