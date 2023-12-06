# %% A.33.3. Constructor overloading

class Mountain:
    def __init__(self, name = "", region = "", elevation = 0):
        self.name = name
        self.region = region
        self.elevation = elevation
    
    def info(self):
        print(f"name: {self.name}")
        print(f"region: {self.region}")
        print(f"elevation: {self.elevation}m")

mount_everest = Mountain("Everest", "Asia", 8848)
mount_everest.info()

mount_kilimanjaro = Mountain("Kilimanjaro", "Africa")
mount_kilimanjaro.elevation = 5895
mount_kilimanjaro.info()

mount_aconcagua = Mountain(name="Aconcagua", elevation=6961)
mount_aconcagua.region = "South America"
mount_aconcagua.info()

mount_kosciuszko = Mountain()
mount_kosciuszko.name = "Kosciuszko"
mount_kosciuszko.region = "Australia"
mount_kosciuszko.elevation = 2228
mount_kosciuszko.info()
