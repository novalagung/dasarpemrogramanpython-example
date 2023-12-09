# %% A.32.1. List comprehension → ◉ Contoh #1

seq = []
for i in range(5):
    seq.append(i * 2)
print(seq)

seq = [i * 2 for i in range(5)]
print(seq)
