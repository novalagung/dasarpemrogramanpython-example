# %% A.31.1. List comprehension → ◉ Contoh #3

seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)
print(seq)

# %%

seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))
print(seq)

seq = [((i * (2 if i % 2 == 0 else 3))) for i in range(1, 10)]
print(seq)
