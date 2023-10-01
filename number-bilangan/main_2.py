# %% A.17.2. Hexadecimal, Octal, Binary

angka = 140
angka_heksadesimal = 0x8c
angka_oktal = 0o214
angka_biner = 0b10001100

print(f"angka: {angka}")
print(f"heksadesimal: {angka_heksadesimal}")
print(f"oktal: {angka_oktal}")
print(f"biner: {angka_biner}")

print(f"angka {angka:d}")
print(f"heksadesimal: {angka_heksadesimal:x}")
print(f"oktal: {angka_oktal:o}")
print(f"biner: {angka_biner:b}")

# %% ◉ Operasi perbandingan antar basis tertentu menggunakan suffix

if angka == angka_biner:
    print(f"angka {angka} sama dengan biner {angka_biner:b}")

# %% ◉ Print nilai numerik dalam basis tertentu

print(f"angka: {angka_oktal:d}")
print(f"heksadesimal: {angka_oktal:x}")
print(f"oktal: {angka_oktal:o}")
print(f"biner: {angka_oktal:b}")

# %% ◉ Operasi aritmatika antar basis

total = angka + angka_heksadesimal + angka_oktal + angka_biner
print(f"total: {total} (hex: {total:x}, oct: {total:o}, bin: {total:b})")

# %% ◉ Print nilai numerik dalam basis tertentu menggunakan fungsi

int1 = oct(140)
print(f"int1: {int1}")

int2 = oct(0x8c)
print(f"int2: {int2}")

int3 = hex(140)
print(f"int3: {int3}")

int4 = hex(0b10001100)
print(f"int4: {int4}")

int5 = bin(140)
print(f"int5: {int5}")

int6 = bin(0o214)
print(f"int6: {int6}")

# %% ◉ Fungsi int()

int1 = int("0b10001100", base=2)
print(f"int1: {int1}")

int2 = int("0x8c", base=16)
print(f"int2: {int2}")

# %%
