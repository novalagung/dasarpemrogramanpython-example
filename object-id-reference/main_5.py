# %% A.21.5. Reference pada data hasil slicing

numbers1 = [1, 2, 3, 4]
numbers2 = numbers1
numbers3 = numbers1[:]

print("numbers1", numbers1, id(numbers1))
print("numbers2", numbers2, id(numbers2))
print("numbers3", numbers3, id(numbers3))

numbers2.append(9)

print("numbers1", numbers1, id(numbers1))
print("numbers2", numbers2, id(numbers2))
print("numbers3", numbers3, id(numbers3))

# %%
