# %% A.58.3. Custom iterator

from collections.abc import Iterator

class LoopReverse(Iterator):

    def __init__(self, data):
        self.data = data
        self.i = 0

    def __next__(self):
        if (self.i+1) > len(self.data):
            raise StopIteration
        else:
            r = self.data[len(self.data)-self.i-1]
            self.i = self.i + 1
            return r

numbers = [23, 2, 1, 54]
for n in LoopReverse(numbers):
    print(n)

# %%

numbers = [23, 2, 1, 54]
numbers_iter = LoopReverse(numbers)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)

n = next(numbers_iter)
print(n)

# %%

class LoopReverse:

    def __init__(self, data):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.i+1) > len(self.data):
            raise StopIteration
        else:
            r = self.data[len(self.data)-self.i-1]
            self.i = self.i + 1
            return r

numbers = [23, 2, 1, 54]
for n in LoopReverse(numbers):
    print(n)
