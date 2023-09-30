# %% A.21.4. Reference data sequence & slicing

numbers1 = [1, 2, 3, 4]
print("numbers1", id(numbers1), numbers1)

numbers2 = numbers1
print("numbers1", id(numbers1), numbers1)
print("numbers2", id(numbers2), numbers2)

# %%

import sys

numbers1 = [1, 2, 3, 4]
print("numbers1", numbers1, id(numbers1), sys.getsizeof(numbers1))

numbers2 = numbers1
numbers2.append(9)

print("numbers1", numbers1, id(numbers1), sys.getsizeof(numbers1))
print("numbers2", numbers1, id(numbers2), sys.getsizeof(numbers2))
