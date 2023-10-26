# %% A.31.3. Naming convention method & parameter

class FavoriteFood:
    def __init__(self):
        self.name = ""

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

FavoriteFood.get_name()