# %% A.36.1. Attributes

# %% ◉ Instance attribute

class Pencil:

    def __init__(self):
        self.note = "A class type to represent a book"

pencil1 = Pencil()
print(f"Object pencil1 note: {pencil1.note}")

# %% ◉ Class attribute

class Book:
    note = "A class type to represent a book"

print(f"Class Book note: {Book.note}")

# %%

class Book:
    note = "A class type to represent a book"

print(f"Class Book note: {Book.note}")

book1 = Book()
print(f"Object book1 note: {book1.note}")

# %% Kombinasi instance attribute & class attribute

class Song:
    note = "A class type to represent a song"
    version = 1.0
    
    def __init__(self, name = "", artist = "", album = "", released_year = 2000):
        self.name = name
        self.artist = artist
        self.album = album
        self.released_year = released_year

    def info(self):
        print(f"Song: {self.name} by {self.artist}")
        print(f"Album: {self.album}")
        print(f"Released year: {self.released_year}")

songs = [
    Song(
        name="The Ytse Jam",
        artist="Dream Theater",
        album="When Dream and Day Unite",
        released_year=2004
    ),
    Song(
        name="Always with Me, Always with You",
        artist="Joe Satriani",
        album="Surfing with the Alien",
        released_year=1987
    ),
]

print(f"Class: Song, version: {Song.version}, note: {Song.note}")

for s in songs:
    s.info()
