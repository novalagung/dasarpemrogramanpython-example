# %% A.59.3. Generator expression

exp1 = [num**2 for num in range(5)]
print(exp1)

exp2 = (num**2 for num in range(5))
print(exp2)

for d in exp2:
    print(d)

# %%
