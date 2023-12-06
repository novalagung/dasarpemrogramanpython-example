# %% A.31.3. Property ➜ Attribute

class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

car1 = Car()
print(f"car1 name: {car1.name}")
print(f"car1 manufacturer: {car1.manufacturer}")
print(f"car1 year: {car1.year}")
