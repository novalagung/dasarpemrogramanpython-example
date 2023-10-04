# %% A.22.2. Parameter dan argument fungsi

def calculate_circle_area(r):
    area = 3.14 * (r ** 2)
    print("area of circle:", area)

calculate_circle_area(788)

def calculate_circle_area(message: str, r: int):
    area = 3.14 * (r ** 2)
    print(message, area)

calculate_circle_area("area of circle:", 788)

# %%
