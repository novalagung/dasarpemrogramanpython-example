# %% basic

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self):
        self.name = "common vehicle"
        self.number_of_wheels = 4
    
    def drive_sound(self):
        return "vroom vroooommmm"
    
class ElectricCar(Vehicle):
    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())
        
v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels, "wheels. engine sound:", v1.drive_sound())

v2 = ElectricCar()
v2.name = "electric car"
v2.info()

# %% constructor override error

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self):
        self.name = "common vehicle"
        self.number_of_wheels = 4
    
    def drive_sound(self):
        return "vroom vroooommmm"
    
class ElectricCar(Vehicle):
    
    def __init__(self):
        self.name = "electric car"

    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())
        
v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels, "wheels. engine sound:", v1.drive_sound())

v2 = ElectricCar()
v2.info()

# %% constructor override

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

# %% costructor super with params

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self, name = "common vehicle", number_of_wheels = 4):
        self.name = name
        self.number_of_wheels = number_of_wheels
    
    def drive_sound(self):
        return "vroom vroooommmm"

class ElectricCar(Vehicle):
    
    def __init__(self):
        super().__init__(name="electric car")

    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())
    
    def drive_sound(self):
        # return super().drive_sound()
        return "zzzzzzz"
        
v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels, "wheels. engine sound:", v1.drive_sound())

v2 = ElectricCar()
v2.info()

# %% nested inheritance

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self, name = "common vehicle", number_of_wheels = 4):
        self.name = name
        self.number_of_wheels = number_of_wheels
    
    def drive_sound(self):
        return "vroom vroooommmm"
    
class Car(Vehicle):
    pass

class ElectricCar(Car):
    
    def __init__(self):
        super().__init__(name="electric car")

    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())
    
    def drive_sound(self):
        # return super().drive_sound()
        return "zzzzzzz"
        
v1 = Vehicle()
print(v1.name, "has", v1.number_of_wheels, "wheels. engine sound:", v1.drive_sound())

v2 = ElectricCar()
v2.info()

# %% mro

print(ElectricCar.__mro__)

# %% multiple inheritance

class Vehicle:
    note = "class to represent a car"
    
    def __init__(self, name = "common vehicle", number_of_wheels = 4):
        self.name = name
        self.number_of_wheels = number_of_wheels

from typing import Final

ENGINE_ELECTRIC: Final = "electric engine"
ENGINE_PETROL: Final = "petrol engine"
ENGINE_DIESEL: Final = "diesel engine"

class Engine:
    note = "class to represent engine"
    
    def __init__(self, engine_name):
        self.engine_name = engine_name
    
    def drive_sound(self):
        if self.engine_name == ENGINE_ELECTRIC:
            return "zzzzzzz"
        elif self.engine_name == ENGINE_PETROL:
            return "vroom vroooommmm"
        elif self.engine_name == ENGINE_DIESEL:
            return "VROOM VROOM VROOOOMMM"


class ElectricCar(Vehicle, Engine):
    
    def __init__(self):
        Vehicle.__init__(self, "electric car", 4)
        Engine.__init__(self, ENGINE_ELECTRIC)

    def info(self):
        print(v2.name, "has", v2.number_of_wheels, "wheels. engine sound:", v2.drive_sound())

v2 = ElectricCar()
v2.info()

# %%
