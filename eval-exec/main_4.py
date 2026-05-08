# %% A.57.4. Alternatif aman: ast.literal_eval()

import ast

# aman: mengevaluasi literal dict
data = ast.literal_eval("{'name': 'Noval', 'age': 30}")
print(data)
print(type(data))

# aman: mengevaluasi literal list
numbers = ast.literal_eval("[1, 2, 3, 4, 5]")
print(numbers)

# aman: mengevaluasi literal tuple
coord = ast.literal_eval("(10, 20)")
print(coord)

# aman: mengevaluasi tipe data primitif
value = ast.literal_eval("3.14")
print(value)
