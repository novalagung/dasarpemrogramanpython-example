# %%

def say_hello():
    print("hello")

say_hello()

# %%

def calculate_circle_area(r):
    area = 3.14 * (r ** 2)
    return area

def calculate_circle_circumference(r):
    return 2 * 3.14 * r

area = calculate_circle_area(788)
print(f"area: {area:.2f}")

circumference = calculate_circle_circumference(788)
print(f"circumference: {circumference:.2f}")

# %%

# need to complete sometime later
def transpose_matrix(matrix):
    pass

# %%

def transpose_matrix(matrix):
    transposed = []
    for i in range(4):
        tr = []
        for row in matrix:
            tr.append(row[i])
        transposed.append(tr)

    return transposed

def print_matrix(matrix = []):
    for el in matrix:
        print(el)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("matrix:")
print_matrix(matrix)

print()
print("transposed matrix:")
res = transpose_matrix(matrix)
print_matrix(res)

# %%

optional & positional argument

https://realpython.com/defining-your-own-python-function/#keyword-only-arguments