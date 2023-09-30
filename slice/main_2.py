# %% A.20.2. Fungsi `slice()`

data_list = [2, 4, 6, 7, 9, 11, 13]
print(data_list)

list1 = data_list[2:6:1]
print(list1)

list2 = data_list[slice(2, 6, 1)]
print(list2)

sl = slice(2, 6)
list3 = data_list[sl]
print(list3)
