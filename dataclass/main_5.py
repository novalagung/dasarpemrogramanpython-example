# %% A.43.5. Frozen data class

from dataclasses import dataclass

@dataclass(frozen=True)
class Fruit:
    name: str
    flavor: tuple

apple = Fruit("Apple", ("sweet", "tart"))
apple.name = "Orange"
