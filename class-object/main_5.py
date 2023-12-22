# %% A.33.5. Pengecekan instance object

class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

car1 = Car()
car1.name = "M3 GTR"
car1.manufacturer = "BMW"
car1.year = 2001

if isinstance(car1, Car):
    print(f"car1 class is Car")

if isinstance(car1, Car):
    print(f"car1 class is Car")
