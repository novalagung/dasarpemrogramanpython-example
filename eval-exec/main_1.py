# %% A.56.1. Fungsi `eval()`

a = 10
b = 5
c = 8
area = eval('(a + b) / 20 + (c * c)')
print(area)

# %%

try:
    area = eval('(a + b asd / 20 + (c * c)')
except Exception as err:
    print(f"error: {err}")

# %%

area = eval('PI * r * r', { "PI": 3.14, "r": 10 })
print(area)

# %%

PI = 3.14
area = eval('PI * r * r', globals(), { "r": 10 })
print(area)

# %%
