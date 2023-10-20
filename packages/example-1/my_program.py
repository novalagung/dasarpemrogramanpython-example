a = 10
b = 15

import libs.calculate
import libs.common.number
import libs.common.message

print(libs.calculate.note)
print(libs.common.number.note)
print(libs.common.message.note)

res = libs.calculate.calc_hypotenuse(a, b)
libs.common.message.print_hypotenuse(res)

res = libs.common.number.sqrt(a**2 + b**2)
libs.common.message.print_hypotenuse(res)

res = libs.common.number.sqrt(libs.common.number.pow(a) + libs.common.number.pow(b))
libs.common.message.print_hypotenuse(res)
