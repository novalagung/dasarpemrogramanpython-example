# %% A.38.1. Static Method

class Person:

    def __init__(self, name = ""):
        self.name = name

    def info(self):
        print(f"{self.name}")

    @classmethod
    def create(cls, name = ""):
        obj = cls()
        obj.name = name
        return obj
    
    @staticmethod
    def say_hello():
        print("hello")
    
    @staticmethod
    def say_something(message, name = None):
        if name != None:
            print(f"{name} said: {message}")
        else:
            print(message)

p1 = Person.create("Kassandra")
p1.say_hello()
Person.say_hello()

p2 = Person("Edward Kenway")
p2.say_something("hello folks! #1")
p2.say_something("hello folks! #2", p2.name)
Person.say_something("hello folks! #3")
