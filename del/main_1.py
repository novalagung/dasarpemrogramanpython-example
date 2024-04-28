# %% A.54.1. Keyword `del`

name = "Noval Agung"
print(name)

del name
print(name)

# %% ◉ Delete list item

obj = ["Noval", "Malang", "Chad"]
print(obj)

del obj[1]
print(obj)

# %% ◉ Delete dictionary item

obj = {
    "name": "Noval",
    "city": "Malang",
    "gender": "Chad"
}
print(obj)

del obj["city"]
print(obj)

del obj["gender"]
print(obj)

# %% ◉ Delete class/object property

class Person:
    def __init__(self, name, city, gender):
        self.name = name
        self.city = city
        self.gender = gender

p = Person("Noval", "Malang", "Chad")
print(p.name, p.city, p.gender)

try:
    del p.city
    print(p.name, p.city, p.gender)

except Exception as err:
    print(err)

# %% ◉ Delete function

def say_hello():
    print("hello world")

say_hello()

try:
    del say_hello
    say_hello()

except Exception as err:
    print(err)

# %% ◉ Delete class

class Person:
    def __init__(self, name, city, gender):
        self.name = name
        self.city = city
        self.gender = gender

p = Person("Noval", "Malang", "Chad")
print(p.name, p.city, p.gender)

try:
    del Person
    p = Person("Noval", "Malang", "Chad")

except Exception as err:
    print(err)
