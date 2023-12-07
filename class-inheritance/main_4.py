# %% A.39.4. Method Overriding

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self):
        self.name = "common vehicle"
        self.number_of_wheels = 4
    
    def drive_sound(self):
        return "vroom vroooommmm"
    
class ElectricCar(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.name = "electric car"

    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())
    
    def drive_sound(self):
        return "zzzzzzz"

v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels, "wheels. engine sound:", v1.drive_sound())

v2 = ElectricCar()
v2.info()
