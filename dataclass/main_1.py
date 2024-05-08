# %% A.43.1. Pengenalan Data Class

class Planet:
    def __init__(self, name, diameter, natural_sattelites):
        self.name = name
        self.diameter = diameter
        self.natural_sattelites = natural_sattelites

planets = [
    Planet("Mercury", 4879, []),
    Planet(name="Venus", diameter=12104, natural_sattelites=[]),
    Planet(diameter=12742, name="Earth", natural_sattelites=["Moon"]),
]

for p in planets:
    print(f"{p.name} | {p.diameter} km | {len(p.natural_sattelites)} moons")

# %%

from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    diameter: float
    natural_sattelites: list[str]

planets = [
    Planet("Mercury", 4879, []),
    Planet("Venus", 12104, []),
    Planet("Earth", 12742, ["Moon"]),
]

for p in planets:
    print(f"{p.name} | {p.diameter} km | {len(p.natural_sattelites)} moons")
