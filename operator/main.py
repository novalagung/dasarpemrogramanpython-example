#%% operator aritmatika

num = 2 + 2
print("2 + 2 = %d" % (num))

num = 3 - 2
print("3 - 2 = %d" % (num))

num = 3 * 3
print("3 * 3 = %d" % (num))

num = 8 / 2
print("8 / 2 = %d" % (num))

num = 10 // 3
print("10 // 3 = %d" % (num))

num = 7 % 4
print("7 %% 4 = %d" % (num))

num = 3 ** 2
print("3 ** 2 = %d" % (num))

#%% operator assignment

num_1 = 12
num_2 = 24

num_2 = 12
num_3 = num_1 + num_2

print(num_3)
# output: 24

#%% operator perbandingan

res = 4 == 5
print("4 == 5 =", res)

res = 4 != 5
print("4 != 5 =", res)

res = 4 > 5
print("4 > 5 =", res)

res = 4 < 5
print("4 < 5 =", res)

res = 5 >= 5
print("5 >= 5 =", res)

res = 4 <= 5
print("4 <= 5 =", res)

#%% operator logika

res = (4 == 5) and (2 != 3)
print("(4 == 5) and (2 != 3) =", res)

res = (4 == 5) or (2 != 3)
print("(4 == 5) and (2 != 3) =", res)

res = not (2 == 3)
print("not 2 == 3 =", res)

#%% operator identity

num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

#%% fungsi `print()` tanpa output formatting

print("message: %s %s %s" % ("hello", "python", "learner"))
print("message:", "hello", "python", "learner")

#%% fungsi `id()`

data_1 = "hello world"
id_data_1 = id(data_1)
print("data_1:", data_1)        # hello world
print("id_data_1:", id_data_1)  # 19441xxxxxxxx

#%% operator membership

# membership check in list
sample_list = [2, 3, 4]
print(3 in sample_list) # prints False

# membership check in tuple
sample_tuple = ("hello", "rust")
print("hello" in sample_tuple) # prints True

# membership check in dictionary
sample_dict = { "nama": "noval", "age": 12 }
print("nama" in sample_dict) # True

# membership check in sets
sample_set = { "sesuk", "preiiii" }
print("preiiii" in sample_set) # True

# substring check
print('orl' in 'Hello world') # True

# %%
