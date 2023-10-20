a = 10
b = 15

import libs.calculate as calc
import libs.common.number as num
import libs.common.message as msg

print(calc.note)
print(num.note)
print(msg.note)

res = calc.calc_hypotenuse(a, b)
msg.print_hypotenuse(res)

res = num.sqrt(a**2 + b**2)
msg.print_hypotenuse(res)

res = num.sqrt(num.pow(a) + num.pow(b))
msg.print_hypotenuse(res)
