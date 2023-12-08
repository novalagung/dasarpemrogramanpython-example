# %% A.40.1. Pengenalan abstract method

class Object2D:
    def calculate_area(self):
        pass

class Triangle(Object2D):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculate_area(self):
        return 1/2 * self.b * self.h

class Circle(Object2D):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r * self.r

obj1 = Triangle(4, 10)
area = obj1.calculate_area()
print(f"area of {type(obj1).__name__}: {area}")

obj2 = Circle(20)
area = obj2.calculate_area()
print(f"area of {type(obj2).__name__}: {area}")

# %%

class Square(Object2D):
    def __init__(self, s):
        self.s = s

obj1 = Triangle(4, 10)
area = obj1.calculate_area()
print(f"area of {type(obj1).__name__}: {area}")

obj2 = Circle(20)
area = obj2.calculate_area()
print(f"area of {type(obj2).__name__}: {area}")

obj3 = Square(6)
area = obj3.calculate_area()
print(f"area of {type(obj3).__name__}: {area}")
