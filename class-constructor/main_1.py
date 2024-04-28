# %% A.35.1. Pengenalan construktor

class Mountain:
    pass

mount_everest = Mountain()
print(mount_everest)

mount_kilimanjaro = Mountain()
print(mount_kilimanjaro)

# %%

class Mountain:
    def __init__(self):
        self.name = ""
        self.region = ""
        self.elevation = 0
    
    def info(self):
        print(f"name: {self.name}")
        print(f"region: {self.region}")
        print(f"elevation: {self.elevation}m")

mount_everest = Mountain()
mount_everest.name = "Everest"
mount_everest.region = "Asia"
mount_everest.elevation = 8848
mount_everest.info()

mount_kilimanjaro = Mountain()
mount_kilimanjaro.name = "Kilimanjaro"
mount_kilimanjaro.region = "Africa"
mount_kilimanjaro.elevation = 5895
mount_kilimanjaro.info()
