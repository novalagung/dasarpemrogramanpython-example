# %%

from abc import ABC, abstractmethod, abstractproperty

class Object2D(ABC):
    @abstractmethod
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

    # def calculate_area(self):
    #     return 3.14 * self.r * self.r

def do_the_math(cls: Object2D):
    area = cls.calculate_area()
    print(f"area of {cls.__class__.__name__}: {area}")

obj1 = Triangle(4, 10)
do_the_math(obj1)

obj2 = Circle(20)
do_the_math(obj2)

# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python/13646263#13646263
