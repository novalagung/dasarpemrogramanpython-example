# A.12.3. Operasi pada list

# %% ◉ Mengakses element via index

list_1 = [10, 70, 20]
elem_1st = list_1[0]
elem_2nd = list_1[1]
elem_3rd = list_1[2]

print(elem_1st, elem_2nd, elem_3rd)

# %% ◉ Slicing list

list_2 = ['ab', 'cd', 'hi', 'ca']
slice_1 = list_2[1:3]
print('slice_1:', slice_1)

# %% ◉ Mengubah nilai element

list_2 = ['ab', 'cd', 'hi', 'ca']
print('before:', list_2)

list_2[1] = 'zk'
list_2[2] = 'sa'
print('after:', list_2)

# %% ◉ Append element

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1.append(88)
list_1.append(87)
print('after: ', list_1)

# %% ◉ Append element

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1[len(list_1):] = [88, 87]
print('after: ', list_1)

# %% ◉ Extend/concat element

list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1.extend(list_2)
print(list_1)

# %% ◉ Extend/concat element

list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1[len(list_1):] = list_2
print(list_1)

# %% ◉ Extend/concat element

list_1 = [10, 70, 20]
list_2 = [88, 77]
list_3 = list_1 + list_2
print(list_3)

# %% ◉ Menyisipkan element pada index `i`

list_3 = [10, 70, 20, 70]
list_3.insert(0, 15)
print(list_3)
list_3.insert(2, 25)
print(list_3)

# %% ◉ Menghapus element

list_3 = [10, 70, 20, 70]
list_3.remove(70)
print(list_3)
list_3.remove(70)
print(list_3)

# %% ◉ Menghapus element pada index `i`

list_3 = [10, 70, 20, 70]

x = list_3.pop(2)
print('list_3:', list_3)
print('removed element:', x)

x = list_3.pop()
print('list_3:', list_3)
print('removed element:', x)

# %% ◉ Menghapus element pada index `i`

list_3 = [10, 70, 20, 70]

del list_3[1:3]
print(list_3)

# %% ◉ Menghitung jumlah element

list_3 = [10, 70, 20, 70]
total = len(list_3)
print(total)

# %% ◉ Menghitung jumlah element

list_3 = [10, 70, 20, 70]
count = list_3.count(70)
print('jumlah element dengan data `70`:', count)

# %% ◉ Mencari index element list

list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st = list_2.index('cd')
print('idx_1st index:', idx_1st)

# %% ◉ Mencari index element list

idx_2nd = list_2.index('kk')
print('idx_2nd: ', idx_2nd)

# %% ◉ Mengosongkan list

list_1 = [10, 70, 20]
list_1.clear()
print(list_1)

# %% ◉ Mengosongkan list

list_1 = [10, 70, 20]
list_1 = []
print(list_1)

# %% ◉ Mengosongkan list

list_1 = [10, 70, 20]
del list_1[:]
print(list_1)

# %% ◉ Membalik urutan element list

list_1 = [10, 70, 20]
list_1.reverse()
print(list_1)

# %% ◉ Duplikasi list

list_1 = [10, 70, 20]
list_2 = list_1.copy()
print(list_1)
print(list_2)

list_1 = [10, 70, 20]
list_2 = list_1[:]
print(list_1)
print(list_2)

# %% ◉ Sorting

list_1 = [10, 70, 20]
list_1.sort()
print(list_1)

list_2 = ['z', 'h', 'c']
list_2.sort()
print(list_2)
