a = 10
b = 15

import calculate

print(calculate.note)

res = calculate.calc_hypotenuse(a, b)
print("hypotenuse:", res)

res = calculate.sqrt(a**2 + b**2)
print("hypotenuse:", res)

res = calculate.sqrt(calculate.pow(a) + calculate.pow(b))
print("hypotenuse:", res)
