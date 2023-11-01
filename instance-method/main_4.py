# %% A.31.5. Pengaksesan method via class

class FavoriteFood:
    def __init__(self):
        self.name = ""

    def print_name(self):
        print(self.name)

    def get_name(self) -> str:
        return self.name

    def set_name(self, name):
        self.name = name

food1 = FavoriteFood()
food1.set_name("Pizza")
food1.print_name()
print(food1.get_name())

FavoriteFood.set_name(food1, "Burger")
FavoriteFood.print_name(food1)
print(food1.get_name())

# %%
