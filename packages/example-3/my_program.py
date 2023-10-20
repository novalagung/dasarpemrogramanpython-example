a = 10
b = 15

from libs import calculate as calc
from libs.common import number, message

print(calc.note)
print(number.note)
print(message.note)

res = calc.calc_hypotenuse(a, b)
message.print_hypotenuse(res)

res = number.sqrt(a**2 + b**2)
message.print_hypotenuse(res)

res = number.sqrt(number.pow(a) + number.pow(b))
message.print_hypotenuse(res)
