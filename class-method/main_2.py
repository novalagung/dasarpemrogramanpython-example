# %% A.38.2. Class method parameter

class ClanHouse:

    def __init__(self, name = "", house = ""):
        self.name = name
        self.house = house

    @classmethod
    def create(cls, name = "", house = ""):
        obj = cls()
        obj.name = name
        obj.house = house
        return obj

    def info(self):
        print(f"{self.name} of {self.house}")

p2 = ClanHouse("Lady Jessica", "Bene Gesserit")
p2.info()

p4 = ClanHouse.create("Glossu Rabban", "House of Harkonnen")
p4.info()
