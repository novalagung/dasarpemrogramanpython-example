# %% A.57.3. Fungsi `compile()`

a = 10
b = 5
c = 8
compiled = compile('(a + b) / 20 + (c * c)', '<string>', 'eval')
area = eval(compiled)
print(area)

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
compiled = compile(stmt, '<string>', 'exec')
area = exec(compiled)
print(res)
