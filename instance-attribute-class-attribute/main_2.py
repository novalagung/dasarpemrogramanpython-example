# %% A.35.2. Attribute lookup

class Person:
    name = "A person"
    
    def __init__(self, name):
        self.name = name

person1 = Person("Noval Agung Prayogo")
print(f"Object person1 name: {person1.name}")

print(f"Class Person name: {Person.name}")
