# %%

def say_hello1():
    print("hello python")

say_hello2 = lambda : print("hello python")

say_hello1()
say_hello2()

# %%

def get_full_name1(first_name, last_name):
    return f"{first_name} {last_name}"

get_full_name2 = lambda first_name, last_name : f"{first_name} {last_name}"

res = get_full_name1("Darion", "Mograine")
print(res)

res = get_full_name2("Sally", "Whitemane")
print(res)

# %%

def transpose_matrix1(m):
    tm = []
    for i in range(len(m[0])):
        tr = []
        for row in m:
            tr.append(row[i])
        tm.append(tr)
    return tm

transpose_matrix2 = lambda m : [[row[i] for row in matrix] for i in range(len(m[0]))]

matrix = [[1, 2], [3, 4], [5, 6]]

res = transpose_matrix1(matrix)
print(res)

res = transpose_matrix2(matrix)
print(res)

# %%

def debug1(separator, *params):
    res = []
    for i in range(len(params)):
        res.append(f"param {i}: {params[i]}")
    return separator.join(res)

debug2 = lambda separator, *params : separator.join([f"param {i}: {params[i]}" for i in range(len(params))])

res = debug1(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)

res = debug2(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)

# %%

def debug3(separator, **params):
    res = []
    for key in params:
        res.append(f"{key}: {params[key]}")
    return separator.join(res)

debug4 = lambda separator, **params : separator.join([f"{key}: {params[key]}" for key in params])

res = debug3(", ", name="Darion Mograine", occupations=["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], active=True)
print(res)

res = debug4(", ", name="Darion Mograine", occupations=["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], active=True)
print(res)

# %%

def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")

def average1(numbers):
    return sum(numbers) / len(numbers)

average2 = lambda numbers : sum(numbers) / len(numbers)

numbers = [24, 67, 22, 98, 3, 50]

aggregate("average", numbers, average1)
aggregate("average", numbers, average2)
aggregate("average", numbers, lambda numbers : sum(numbers) / len(numbers))

# %%
