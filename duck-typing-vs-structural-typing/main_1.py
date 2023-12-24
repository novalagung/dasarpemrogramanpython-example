# %% A.43.1. Pengenalan duck typing

def do_the_math(obj):
    area = obj.calculate_area()
    print(f"area of {type(obj).__name__}: {area}")

# %% ◉ Skenario 1: Instance method

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculate_area(self):
        return 1/2 * self.b * self.h

obj1 = Triangle(4, 10)
do_the_math(obj1)

# %% ◉ Skenario 2: Attribute berisi closure

def number_10():
    return 10

class AreaOf2x10:
    def __init__(self) -> None:
        self.calculate_area = number_10

obj2 = AreaOf2x10()
do_the_math(obj2)

# %% ◉ Skenario 3: Attribute berisi lambda

import random
class AreaOfRandomInt:
    def __init__(self) -> None:
        self.calculate_area = lambda : random.randint(0, 10) * 2

obj3 = AreaOfRandomInt()
do_the_math(obj3)

# %% ◉ Skenario 4: Class method

class NotReallyA2dObject:
    @classmethod
    def calculate_area(cls):
        return "where is the number?"

do_the_math(NotReallyA2dObject)
