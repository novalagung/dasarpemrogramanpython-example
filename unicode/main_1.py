# %% A.18.1. Penerapan Unicode

message = "안녕하세요 😀"
print(message)

message = "\uC548\uB155\uD558\uC138\uC694"
print(message)

message = "\U0000C548\U0000B155\U0000D558\U0000C138\U0000C694 \U0001F600"
print(message)

message = "\N{HANGUL SYLLABLE AN}\N{HANGUL SYLLABLE NYEONG}\N{HANGUL SYLLABLE HA}\N{HANGUL SYLLABLE SE}\N{HANGUL SYLLABLE YO} \N{GRINNING FACE}"
print(message)
