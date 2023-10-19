a = 10
b = 15

from calculate import *

print(note)

res = calc_hypotenuse(a, b)
print("hypotenuse:", res)

res = sqrt(a**2 + b**2)
print("hypotenuse:", res)

res = sqrt(pow(a, 2) + pow(b, 2))
print("hypotenuse:", res)
