# %% calculate

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculate_area(self):
        return 1/2 * self.b * self.h

class Circle:
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r * self.r

def do_the_math(cls):
    area = cls.calculate_area()
    print(f"area of {cls.__class__.__name__}: {area}")

obj1 = Triangle(4, 10)
do_the_math(obj1)

obj2 = Circle(20)
do_the_math(obj2)

# %%

class NotReallyA2dObject:
    def calculate_area(self):
        return "??"

obj3 = NotReallyA2dObject()
do_the_math(obj3)
# %%
