# %% A.18.2. Fungsi utilitas pada *Unicode*

# %% Fungsi `ord()`

text = "안"
codePoint = ord(text)
print(f'code point of {text} in decimal: {codePoint}')

text = "N"
codePoint = ord(text)
print(f'code point of {text} in decimal: {codePoint}')

text = "안"
codePoint = ord(text)
print(f'code point of {text} in decimal: {codePoint}')
print(f'code point of {text} in hex: {hex(codePoint)}')

# %% Fungsi `chr()`

codePoint = chr(50504)
print(codePoint)

codePoint = chr(0xC548)
print(codePoint)
