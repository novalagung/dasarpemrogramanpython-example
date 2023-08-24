# %% A.15.3. Mengakses elemen sets

fellowship = {'aragorn', 'gimli', 'legolas'}

for p in fellowship:
    print(p)

# %% ◉ Eliminasi elemen duplikat - 1

data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)
# output → {1, 2, 3, 4, 5}

# %% ◉ Eliminasi elemen duplikat - 2

data = [2, 3, 2, 1, 4, 5, 2, 1, 3, 5]
print(data)

data_unique_sets = set(data)
print(data_unique_sets)

data_unique = list(data_unique_sets)
print(data_unique)

# %% ◉ Pengecekan membership

fellowship = {'aragorn', 'gimli', 'legolas'}
to_find = 'gimli'

if to_find in fellowship:
    print(to_find, 'is exists within fellowship')
