# %% A.43.2. Attribute mutability

from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    diameter: float
    natural_sattelites: list[str]

mars = Planet("Mars", 4, ["Phobos", "Deimos"])
mars.name = "Red Planet"
mars.diameter = 6779

print(f"{mars.name} | {mars.diameter} km | {len(mars.natural_sattelites)} moons")
