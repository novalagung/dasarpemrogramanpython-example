
# %% Constructor overloading

class Car:
    def __init__(self, name = "", manufacturer = "", year = 2023, description = ""):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.description = description
    
    def set_details(self, year, description):
        self.year = year
        self.description = description

    def get_name(self):
        return f"{self.manufacturer} {self.name}"

    def info(self):
        print(f"Car name: {self.get_name()}")
        print(f"Description: {self.description}")
        print(f"Year released: {self.year}")

all_cars = []

car1 = Car("M3 GTR", "BMW", 2001)
all_cars.append(car1)

car2 = Car(year=2002, manufacturer="Mazda", name="RX-8", description="Best car in NFS Underground 2")
all_cars.append(car2)

car3 = Car()
car3.name = "Le Mans Quattro"
car3.manufacturer = "Audi"
car3.set_details(2003, "Best car in NFS Carbon")
all_cars.append(car3)

for c in all_cars:
    c.info()
    print()

# %% Method alias

def print_car_info(self):
    print(f"Car name: {self.manufacturer} {self.name}")
    print(f"Description: {self.description}")
    print(f"Year released: {self.year}")

class Car:
    def __init__(self, name = "", manufacturer = "", year = 2023, description = ""):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.description = description

    info = print_car_info

all_cars = []

car1 = Car("M3 GTR", "BMW", 2001, "Best car in NFS Most Wanted")
all_cars.append(car1)

car2 = Car("RX-8", "Mazda", 2002, "Best car in NFS Underground 2")
all_cars.append(car2)

car3 = Car("Le Mans Quattro", "Audi", 2003, "Best car in NFS Carbon")
all_cars.append(car3)

for c in all_cars:
    c.info()
    print()

# %%
