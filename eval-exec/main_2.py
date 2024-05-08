# %% A.57.2. Fungsi `exec()`

a = 10
b = 5
c = 8
res = 0
exec('res = (a + b) / 20 + (c * c)')
print(res)

# %%

r = 4
stmt = """
for x in range(r):
    print(x)
"""
exec(stmt)

# %%

r = 10
res = 0
stmt = """
from typing import Final

PI: Final = 3.14

def calculate_area_of_circle():
    print(f"calculating area of circle with r: {r}")
    return PI * r * r

res = calculate_area_of_circle()
"""
exec(stmt)
print(res)

# %%
