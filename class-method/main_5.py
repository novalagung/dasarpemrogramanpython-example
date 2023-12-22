# %% A.38.4. Pengaksesan class attribute via `cls`

class ClanHouse:

    note = "ClanHouse: a class to represent clan house in Dune universe"

    def __init__(self, name = "", house = ""):
        self.name = name
        self.house = house

    @classmethod
    def create(cls, name = "", house = ""):
        print("#1", cls.note)

        obj = cls(name, house)
        print("#2", obj.note)

        return obj

p2 = ClanHouse.create("Lady Jessica", "Bene Gesserit")
print("#3", p2.note)

print("#4", ClanHouse.note)
