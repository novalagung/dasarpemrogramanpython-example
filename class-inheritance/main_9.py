# %% A.41.9. Special name ➜ class attribute `__mro__`

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
        print(self.name, "has", self.number_of_wheels, "wheels. engine sound:", self.drive_sound())

    def drive_sound(self, sound = "zzzzzzz"):
        return ("friendly sound", sound)

print("hirarki class ElectricCar:")
for cls in ElectricCar.__mro__:
    print(f"➜ {cls.__name__}")

print("hirarki class Car:")
for cls in Car.__mro__:
    print(f"➜ {cls.__name__}")

print("hirarki class Vehicle:")
for cls in Vehicle.__mro__:
    print(f"➜ {cls.__name__}")
