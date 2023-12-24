# A.43.4. Pencocokan pola tipe data lainnya

# %% ◉ Pencocokan pola data tuple

import random

def coords_generator(n = 5):
    coords = []
    for _ in range(0, n):
        coords.append((random.randint(-5, 5), random.randint(-5, 5)))
    return coords

data = coords_generator(8)
for c in data:
    match c:
        case (0, 0):
            print(f"coord {c} is positioned at the center")
        case (x, 0) if x < 0:
            print(f"coord {c} is positioned at the left horizontally center")
        case (x, 0) if x > 0:
            print(f"coord {c} is positioned at the right horizontally center")
        case (0, y) if y < 0:
            print(f"coord {c} is positioned at the bottom vertically center")
        case (0, y) if y > 0:
            print(f"coord {c} is positioned at the top vertically center")
        case (-5, 5) | (-5, -5) | (5, -5) | (5, 5):
            print(f"coord {c} is positioned at certain corner")
        case other:
            print(f"coord {other} is positioned at the somewhere")

# %% ◉ Pencocokan pola data dictionary

import random

def coords_generator(n = 5):
    coords = []
    for _ in range(0, n):
        coords.append({
            "x": random.randint(-5, 5),
            "y": random.randint(-5, 5)
        })
    return coords

data = coords_generator(8)
for c in data:
    match c:
        case {"x": 0, "y": 0}:
            print(f"coord {c} is positioned at the center")
        case {"x": x, "y": 0} if x < 0:
            print(f"coord {c} is positioned at the left horizontally center")
        case {"x": x, "y": 0} if x > 0:
            print(f"coord {c} is positioned at the right horizontally center")
        case {"x": 0, "y": y} if y < 0:
            print(f"coord {c} is positioned at the bottom vertically center")
        case {"x": 0, "y": y} if y > 0:
            print(f"coord {c} is positioned at the top vertically center")
        case {"x": -5, "y": 5} | {"x": -5, "y": -5} | {"x": 5, "y": -5} | {"x": 5, "y": 5}:
            print(f"coord {c} is positioned at certain corner")
        case other:
            print(f"coord {other} is positioned at the somewhere")

# %% ◉ Pencocokan pola data object class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def info(self):
        return f"({x},{y})"

import random

def coords_generator(n = 5):
    coords = []
    for _ in range(0, n):
        coords.append(Point(random.randint(-5, 5), random.randint(-5, 5)))
    return coords

data = coords_generator(8)
for c in data:
    match c:
        case Point(x=0, y=0):
            print(f"coord {c.info()} is positioned at the center")
        case Point(x=x, y=0) if x < 0:
            print(f"coord {c.info()} is positioned at the left horizontally center")
        case Point(x=x, y=0) if x > 0:
            print(f"coord {c.info()} is positioned at the right horizontally center")
        case Point(x=0, y=y) if y < 0:
            print(f"coord {c.info()} is positioned at the bottom vertically center")
        case Point(x=0, y=y) if y > 0:
            print(f"coord {c.info()} is positioned at the top vertically center")
        case Point(x=-5, y=5) | Point(x=-5, y=-5) | Point(x=5, y=-5) | Point(x=5, y=5):
            print(f"coord {c.info()} is positioned at certain corner")
        case other:
            print(f"coord {other.info()} is positioned at the somewhere")
