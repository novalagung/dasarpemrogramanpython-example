a = 10
b = 15

from libs import *
from libs.common import *

print(calculate.note)
print(number.note)
print(message.note)

res = calculate.calc_hypotenuse(a, b)
message.print_hypotenuse(res)

res = number.sqrt(a**2 + b**2)
message.print_hypotenuse(res)

res = number.sqrt(number.pow(a) + number.pow(b))
message.print_hypotenuse(res)
