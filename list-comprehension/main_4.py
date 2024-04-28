# %% A.13.1. List comprehension → ◉ Contoh #4

list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)
print(seq)

seq = [x + y for x in list_x for y in list_y]
print(seq)
