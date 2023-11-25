# %% A.35.3. Pengaksesan class method via Instance Object

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

p2 = ClanHouse("Lady Jessica", "Bene Gesserit")
p2.info()

p4 = ClanHouse.create("Glossu Rabban", "House of Harkonnen")
p4.info()

p5 = p2.create("Irulan Corrino", "Corrino Empire")
p5.info()
