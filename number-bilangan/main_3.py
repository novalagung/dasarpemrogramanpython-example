# %% A.17.3. Floating point (float)

angka_float = 3.
print(f"angka float: {angka_float}")

angka_float = 3.141592653589
print(f"angka float: {angka_float}")

# %% ◉ Pembulatan / rounding

pi = -3.141592653589

n1 = round(pi, 2)
print(f"n1: {n1}")

n2 = round(pi, 5)
print(f"n2: {n2}")

import math

n3 = math.floor(pi)
print(f"n3: {n3}")

n4 = math.ceil(pi)
print(f"n4: {n4}")

# %% ◉ Pembulatan float dengan string formatting

angka_float = 3.141592653589

print(f"angka float: {angka_float:.2f}")
print(f"angka float: {angka_float:.3f}")
print(f"angka float: {angka_float:.4f}")

# %% ◉ Karakteristik floating point

n = 3.14 + 2.8
print(f"3.14 + 2.8: {n}")
print(f"3.14 + 2.8: {n:f}")
print(f"3.14 + 2.8: {n:.2f}")

# %% ◉ Fungsi float()

number = 278885
float_num = float(number)
print(f"float_num: {float_num}")

number = '278885.666'
float_num = float(number)
print(f"float_num: {float_num}")

# %% ◉ Exponential float

float1 = 2e0
print(f"float1: {float1}")

float2 = 577e2
print(f"float2: {float2}")

float3 = 68277e+6
print(f"float3: {float3}")

float4 = 6e-3
print(f"float4: {float4}")
