# %% A.56.1. Enum / Enumeration

from enum import Enum
class City(Enum):
    MALANG = 1
    SURABAYA = 2
    YOGYAKARTA = 3
    JAKARTA = 4

print(list(City))

# %% A.56.4. Nilai property enum

city1 = City.YOGYAKARTA
print(city1)
print(f"name {city1.name}")
print(f"value {city1.value}")

city2 = City["SURABAYA"]
print(city2)
print(f"name {city2.name}")
print(f"value {city2.value}")

city3 = City(4)
print(city3)
print(f"name {city3.name}")
print(f"value {city3.value}")

# %% A.56.3. Notasi penulisan pengaksesan enum property

from enum import StrEnum
class Color(StrEnum):
    RED = "red"
    BLUE = "blue"

print(list(Color))

color1 = Color("red")
color2 = Color.RED
color3 = Color["BLUE"]
print(color1, color2, color3)

from enum import IntEnum, auto
class Size(IntEnum):
    S = auto()
    M = auto()
    L = auto()
    XL = auto()

print(list(Size))

size1 = Size.M
size2 = Size.XL
print(size1, size2)

# %% A.56.5. Pengecekan nilai enum

def say_anything(c):
    if c is City.MALANG:
        print("Oyi sam")
    elif c == City.JAKARTA:
        print("lo gue lo gue")
    elif c == City.SURABAYA:
        print("coeg")
    elif c == City.YOGYAKARTA:
        print("monggo")

city1 = City.YOGYAKARTA
say_anything(city1)

# %% A.56.6. Perulangan enum

for c in City:
    print(c, c.name, c.value)
