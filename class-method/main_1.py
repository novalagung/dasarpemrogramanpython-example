# %% A.37.1. Class method

class ClanHouse:

    def __init__(self, name = "", house = ""):
        self.name = name
        self.house = house

    @classmethod
    def create(cls):
        obj = cls()
        return obj

    def info(self):
        print(f"{self.name} of {self.house}")

p1 = ClanHouse()
p1.name = "Paul Atriedes"
p1.house = "House of Atriedes"
p1.info()

p2 = ClanHouse("Lady Jessica", "Bene Gesserit")
p2.info()

p3 = ClanHouse.create()
p3.name = "Baron Vladimir Harkonnen"
p3.house = "House of Harkonnen"
p3.info()
