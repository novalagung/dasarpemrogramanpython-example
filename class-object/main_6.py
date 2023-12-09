# %% A.32.6. Class turunan `object`

class Car:
    def __init__(self):
        self.name = ""

data1 = Car()
if isinstance(data1, Car):
    print(f"data1 class inherit from Car")
if isinstance(data1, object):
    print(f"data1 class inherit from object")

data2 = "Noval Agung"
if isinstance(data2, str):
    print(f"data2 class inherit from str")
if isinstance(data2, object):
    print(f"data2 class inherit from object")
