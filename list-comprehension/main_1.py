# A.12.5. List comprehension

# %% A.12.5. Contoh #1
seq = []
for i in range(5):
    seq.append(i * 2)
print(seq) # output → [0, 2, 4, 6, 8]

seq = [i * 2 for i in range(5)]
print(seq) # output → [0, 2, 4, 6, 8]

# %% A.12.5. Contoh #2
seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)
print(seq) # output → [1, 3, 5, 7, 9]

seq = [i for i in range(10) if i % 2 == 1]
print(seq) # output → [1, 3, 5, 7, 9]

# %% A.12.5. Contoh #3
seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)
print(seq) # output → [3, 4, 9, 8, 15, 12, 21, 16, 27]

seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))
print(seq) # output → [3, 4, 9, 8, 15, 12, 21, 16, 27]

seq = [((i * 2) if i % 2 == 0 else (i * 3)) for i in range(1, 10)]
print(seq) # output → [3, 4, 9, 8, 15, 12, 21, 16, 27]

# %% A.12.5. Contoh #4
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

comb = []
for x in list_x:
    for y in list_y:
        comb.append(x + y)
print(seq) # output → ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

comb = [x + y for x in list_x for y in list_y]
print(seq) # output → ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# %% A.12.5. Contoh #5
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    transposed.append(tr)
print(transposed) # output → [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # output → [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed) # output → [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
