# %% A.26.5. Isi lambda: statement 1 baris

def transpose_matrix1(m):
    tm = []
    for i in range(len(m[0])):
        tr = []
        for row in m:
            tr.append(row[i])
        tm.append(tr)
    return tm

transpose_matrix2 = lambda m : [[row[i] for row in matrix] for i in range(len(m[0]))]

matrix = [[1, 2], [3, 4], [5, 6]]

res = transpose_matrix1(matrix)
print(res)

res = transpose_matrix2(matrix)
print(res)
