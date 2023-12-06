# %% A.19.4. Bilangan *complex*

angka_complex = 120+3j

print(f"angka complex: {angka_complex}")

r = angka_complex.real
print(f"angka real: {r}")

i = angka_complex.imag
print(f"angka imajiner: {i}")

# %% ◉ Fungsi `complex()`

angka_complex = complex(120, 3)
print(f"angka complex: {angka_complex}")

# %% ◉ Operasi aritmatika bilangan *complex*

cmp1 = 120-2j
cmp2 = -19+4j

res = cmp1 + cmp2
print(f"angka complex: {res}")

res = cmp1 + cmp2 + 23
print(f"angka complex: {res}")

res = (cmp1 + cmp2 + 23) / 0.5
print(f"angka complex: {res}")
