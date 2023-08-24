# %% A.15.6. Set comprehension `set()`

res = {x for x in set('abracadabra') if x not in set('abc')}
print(res)
