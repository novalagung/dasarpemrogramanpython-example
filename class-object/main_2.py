# %% A.30.2. Instance object

class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

person1 = Person()
print(f"instance object: {person1}")
print(f"type: {type(person1)}")

# %%

class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

car1 = Car()
car2 = Car()
car3 = Car()
