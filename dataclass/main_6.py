# %% A.43.6. Inheritance

from dataclasses import dataclass

@dataclass
class Animal:
    name: str

@dataclass
class Bird(Animal):
    can_fly: bool

cow = Animal(name="Cow")
print(cow.name)

chicken = Bird(name="Chicken", can_fly=False)
print(chicken.name, chicken.can_fly)
