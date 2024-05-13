# %% A.58.2. Apa itu iterator?

condition = "weteng luwe"
for c in iter(condition):
    print(c)

numbers = [10, 12, 32, 44]
for n in iter(numbers):
    print(n)

# %%

numbers = [10, 12, 32, 44]
numbers_iter = iter(numbers)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)
