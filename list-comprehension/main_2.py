# %% A.13.1. List comprehension → ◉ Contoh #2

seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)
print(seq)

seq = [i for i in range(10) if i % 2 == 1]
print(seq)
