# %% A.34.2. Constructor dengan custom param

class Mountain:
    def __init__(self, name, region, elevation):
        self.name = name
        self.region = region
        self.elevation = elevation
    
    def info(self):
        print(f"name: {self.name}")
        print(f"region: {self.region}")
        print(f"elevation: {self.elevation}m")

mount_everest = Mountain("Everest", "Asia", 8848)
mount_everest.info()

mount_kilimanjaro = Mountain("Kilimanjaro", "Africa", 5895)
mount_kilimanjaro.info()
