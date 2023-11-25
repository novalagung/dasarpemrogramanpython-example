# %% static method

class ClanHouse:

    def __init__(self, name = "", house = ""):
        self.name = name
        self.house = house

    def info(self):
        print(f"{self.name} of {self.house}")

    @classmethod
    def create(cls, name = "", house = ""):
        obj = cls()
        obj.name = name
        obj.house = house
        return obj
    
    @staticmethod
    def say_something(message, obj = None):
        if obj != None:
            print(f"{obj.name} said: {message}")
        else:
            print(message)


p2 = ClanHouse("Lady Jessica", "Bene Gesserit")
p2.say_something("hello folks!")

ClanHouse.say_something("how are you", p2)

# %%
