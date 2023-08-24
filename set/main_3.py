# %% A.15.4. Operasi pada set

# %% ◉ Menambah element

fellowship = set()

fellowship.add('aragorn')
print("len:", len(fellowship), "data:", fellowship)

fellowship.add('gimli')
print("len:", len(fellowship), "data:", fellowship)

fellowship.add('legolas')
print("len:", len(fellowship), "data:", fellowship)

# %% ◉ Menghapus element secara acak

fellowship = {'narya', 'nenya', 'nilya'}

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

# %% ◉ Menghapus spesifik elemen

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print("fellowship:", fellowship)

fellowship.discard('boromir')
print("fellowship:", fellowship)

fellowship.remove('gandalf')
print("fellowship:", fellowship)

fellowship.discard('batman')
print("fellowship:", fellowship)

fellowship.remove('superman')
print("fellowship:", fellowship)

# %% ◉ Mengosongkan isi set

fellowship = {'aragorn', 'gimli', 'legolas'}
fellowship.clear()

print("len:", len(fellowship), "data:", fellowship)

# %% ◉ Copy set

data1 = {'aragorn', 'gimli', 'legolas'}
print("len:", len(data1), "data1:", data1)

data2 = data1.copy()
print("len:", len(data2), "data2:", data2)

# %% ◉ Pengecekan *difference* antar sets

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff = fellowship.difference(hobbits)
print("diff:", diff)

fellowship.difference_update(hobbits)
print("fellowship:", fellowship)

# %% ◉ Pengecekan *intersection* antar sets

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

duplicates = fellowship.intersection(hobbits)
print("duplicates:", duplicates)

fellowship.intersection_update(hobbits)
print("fellowship:", fellowship)

# %% ◉ Pengecekan keanggotaan *subset*

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 = hobbits_1.issubset(fellowship)
print("res_1:", res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin'}
res_2 = hobbits_2.issubset(fellowship)
print("res_2:", res_2)

# %% ◉ Pengecekan keanggotaan *superset*

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 = fellowship.issuperset(hobbits_1)
print("res_1:", res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin'}
res_2 = fellowship.issuperset(hobbits_2)
print("res_2:", res_2)

# %% ◉ Pengecekan keanggotaan *disjoint*

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

res_1 = fellowship.isdisjoint({'aragorn', 'gimli'})
print("res_1:", res_1)

res_2 = fellowship.isdisjoint({'pippin', 'bilbo'})
print("res_2:", res_2)

res_3 = fellowship.isdisjoint({'bilbo'})
print("res_3:", res_3)

# %%

hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimly'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_1 = hobbits.union(dunedain).union(dunedain).union(elf).union(dwarf).union(human).union(maiar)
print("fellowship_1:", fellowship_1)

fellowship_2 = set()
fellowship_2.update(hobbits)
fellowship_2.update(dunedain)
fellowship_2.update(dunedain)
fellowship_2.update(elf)
fellowship_2.update(dwarf)
fellowship_2.update(human)
fellowship_2.update(maiar)
print("fellowship_2:", fellowship_2)

# %%
