# %% A.20.1. Pengenalan slice

data_str = "hello world"
print(data_str)

slice1 = data_str[0:3]
print(slice1)

slice2 = data_str[2:8]
print(slice2)

slice3 = data_str[:5]
print(slice3)

slice4 = data_str[4:]
print(slice4)

slice5 = data_str[3:7:1]
print(slice5)

slice6 = data_str[2:9:2]
print(slice6)

slice7 = data_str[:]
print(slice7)

slice8 = data_str[::2]
print(slice8)

# %% ◉ Tentang slicing seluruh element

data_tuple = (1, 3, 5, 7, 9, 11, 13, 14)
print(data_tuple)

tuple1 = data_tuple[0:len(data_tuple)]
print(tuple1)

tuple2 = data_tuple[0:len(data_tuple):1]
print(tuple2)

tuple3 = data_tuple