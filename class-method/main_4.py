# %% A.38.4. Pengaksesan instance method via Class

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
ClanHouse.info(p2)

p4 = ClanHouse.create("Glossu Rabban", "House of Harkonnen")
ClanHouse.info(p4)

p5 = p2.create("Irulan Corrino", "Corrino Empire")
ClanHouse.info(p5)
