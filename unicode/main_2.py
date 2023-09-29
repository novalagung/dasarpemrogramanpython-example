# %% A.18.2. Fungsi utilitas pada *Unicode*

# %% Fungsi `ord()`

str = "안"
codePoint = ord(str)
print(f'code point of {str} in decimal: {codePoint}')

str = "N"
codePoint = ord(str)
print(f'code point of {str} in decimal: {codePoint}')

str = "안"
codePoint = ord(str)
print(f'code point of {str} in decimal: {codePoint}')
print(f'code point of {str} in hex: {hex(codePoint)}')

# %% Fungsi `chr()`

codePoint = chr(50504)
print(codePoint)

codePoint = chr(0xC548)
print(codePoint)
