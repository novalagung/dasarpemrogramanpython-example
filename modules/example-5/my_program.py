a = 10
b = 15

import calculate as calc
from calculate import calc_hypotenuse as hptns, sqrt

print(calc.note)

res = hptns(a, b)
print("hypotenuse:", res)

res = sqrt(a**2 + b**2)
print("hypotenuse:", res)

res = sqrt(calc.pow(a) + calc.pow(b))
print("hypotenuse:", res)
