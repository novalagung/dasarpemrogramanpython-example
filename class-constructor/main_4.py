# %% A.32.4. Constructor dengan return type `None`

class Mountain:
    def __init__(self, name = "", region = "", elevation = 0) -> None:
        self.name = name
        self.region = region
        self.elevation = elevation
