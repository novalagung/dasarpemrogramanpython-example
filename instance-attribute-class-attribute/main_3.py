# %% A.34.3. Attribute mutability

# %% ◉ Perubahan nilai instance attribute

class Pencil:

    def __init__(self):
        self.note = "A class type to represent a book"

pencil1 = Pencil()
pencil1.note = "A pencil"
pencil2 = Pencil()

print(f"Object pencil1 note: {pencil1.note}")
print(f"Object pencil2 note: {pencil2.note}")

# %% ◉ Perubahan nilai class attribute dari instance object

class Book:
    note = "A class type to represent a book"

book1 = Book()
book2 = Book()
book2.note = "A book"

print(f"Class Book note: {Book.note}")
print(f"Object book1 note: {book1.note}")
print(f"Object book2 note: {book2.note}")
print(f"Class Book note: {Book.note}")

# %% ◉ Perubahan nilai class attribute secara langsung

class Book:
    note = "A class type to represent a book"

book1 = Book()
book2 = Book()

Book.note = "A book"

print(f"Class Book note: {Book.note}")
print(f"Object book1 note: {book1.note}")
print(f"Object book2 note: {book2.note}")
