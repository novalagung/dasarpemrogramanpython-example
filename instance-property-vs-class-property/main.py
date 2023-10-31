# %% Class

class Car:
    note = "A class type to represent Car"

car1 = Car()
print(f"car1 {car1.note}")
print(f"Car's note: {Car.note}")
print()

# %%

class Car:
    note = "A class type to represent Car"

car2 = Car()
car2.note = "Car class is used to create car object"
print(f"car2 {car2.note}")
print(f"Car's note: {Car.note}")
print()

# %%

car3 = Car()

car4 = Car()

Car.note = "A car class"

print(f"car3 {car3.note}")
print(f"car4 {car4.note}")
print(f"Car's note: {Car.note}")
print()

# %% Class Variable

class Car:
    note = "A class type to represent Car"
    actions = []

car1 = Car()
car1.actions.append("drive forward")
print(f"car1 actions: {car1.actions}, note: {car1.note}")
print(f"Car's actions: {Car.actions}")
print()

car2 = Car()
car2.actions.append("turn right")
car2.note = "Car class is used to create car object"
print(f"car1 actions: {car1.actions}, note: {car1.note}")
print(f"car2 actions: {car2.actions}, note: {car2.note}")
print(f"Car's actions: {Car.actions}")

# %% Instance Variable

class Car:
    def __init__(self):
        self.note = "A class type to represent Car"
        self.actions = []

car1 = Car()
car1.actions.append("drive forward")
print(f"car1 actions: {car1.actions}, note: {car1.note}")
print()

car2 = Car()
car2.actions.append("turn right")
car2.note = "Car class is used to create car object"
print(f"car1 actions: {car1.actions}, note: {car1.note}")
print(f"car2 actions: {car2.actions}, note: {car2.note}")
