# %% A.22.4. Tipe data nilai balik fungsi

def calculate_circle_area(r: int) -> float:
    area = 3.14 * (r ** 2)
    return area

def calculate_circle_circumference(r: int) -> float:
    return 2 * 3.14 * r

area = calculate_circle_area(788)
print(f"area: {area:.2f}")

circumference = calculate_circle_circumference(788)
print(f"circumference: {circumference:.2f}")

# %%

# def say_hello() -> None:
#     print("hello world")
#     return None

# def say_hello() -> None:
#     print("hello world")

# def say_hello():
#     print("hello world")
