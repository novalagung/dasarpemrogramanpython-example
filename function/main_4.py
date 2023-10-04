# %% A.22.4. Nilai balik fungsi (return value)

def calculate_circle_area(r: int):
    area = 3.14 * (r ** 2)
    return area

def calculate_circle_circumference(r: int):
    return 2 * 3.14 * r

area = calculate_circle_area(788)
print(f"area: {area:.2f}")

circumference = calculate_circle_circumference(788)
print(f"circumference: {circumference:.2f}")
