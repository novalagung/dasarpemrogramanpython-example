# %% A.14.4. Nested tuple

tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))

for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()
