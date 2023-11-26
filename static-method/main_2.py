# %% A.36.2. Fungsi `staticmethod()`

def say_hello():
    print("hello")

def say_something(message, name = None):
    if name != None:
        print(f"{name} said: {message}")
    else:
        print(message)

class Person:

    def __init__(self, name = ""):
        self.name = name

    say_hello = staticmethod(say_hello)
    say_something = staticmethod(say_something)

p2 = Person("Arno Victor Dorian")
p2.say_hello()
Person.say_hello()

p2 = Person("Adéwalé")
p2.say_something("hello folks! #1")
p2.say_something("hello folks! #2", p2.name)
Person.say_something("hello folks! #3")

# %%

def say_something(message, name = None):
    if name != None:
        print(f"{name} said: {message}")
    else:
        print(message)

class Person:

    def __init__(self, name = ""):
        self.name = name

    greet = staticmethod(say_something)

p5 = Person("Ezio Auditore da Firenze")
p5.greet("hello", p5.name)
Person.greet("hello")
