# %% A.15.5. Fungsi `set()`

data = set('abcd')
print('data', data)

data = set(['a', 'b', 'c', 'd'])
print('data', data)

data = set(('a', 'b', 'c', 'd'))
print('data', data)

data = set(range(1, 5))
print('data', data)

# %% ◉ Operator bitwise dan operator `-` pada set

a = set('abracadabra') # {'c', 'a', 'r', 'd', 'b'}
b = set('alacazam')    # {'c', 'z', 'a', 'm', 'l'}

res = a | b
print(res) # output → {'c', 'z', 'a', 'r', 'd', 'b', 'm', 'l'}

res = a & b
print(res) # output → {'c', 'a'}

res = a ^ b
print(res) # output → {'z', 'r', 'b', 'd', 'm', 'l'}

# %% ◉ Operator `-` pada set

a = set('abracadabra') # {'c', 'a', 'r', 'd', 'b'}
b = set('alacazam')    # {'c', 'z', 'a', 'm', 'l'}

res = a - b
print(res) # output → {'b', 'd', 'r'}
