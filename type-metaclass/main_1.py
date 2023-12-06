# %%

name = "Noval Agung"
t = type(name)
print(f"type: {t.__name__}, data: {name}")

# %%

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f'Hi, I am {self.name}'

p = Person("Noval Agung")
t = type(p)
print(f"type: {t.__name__}, data: {p}")

type()
