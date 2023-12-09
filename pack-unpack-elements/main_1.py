# %% A.46.1. Unpacking Element

# %% ◉ Unpack 1 element = 1 variable

names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
)

soldier1, soldier2, soldier3, warrior1, warrior2, warrior3 = names

print(soldier1)
print(soldier2)
print(soldier3)

print(warrior1)
print(warrior2)
print(warrior3)

# %% ◉ Unpack hanya `N` elements pertama

names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
)

soldier1, soldier2, deceiver1, *warriors = names

print(soldier1)
print(soldier2)
print(deceiver1)
print(warriors)

# %%

names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
)

soldier1, soldier2, deceiver1, *_ = names

print(soldier1)
print(soldier2)
print(deceiver1)

# %% Unpack hanya `N` elements terakhir

names = {
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
}

*soldiers, deceiver1, deceiver2, warrior1, warrior2 = names

print(soldiers)
print(deceiver1)
print(deceiver2)
print(warrior1)
print(warrior2)

# %% ◉ Unpack hanya `N` elements pertama dan terakhir

names = [
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
]

soldier1, soldier2, *deceivers, warrior1, warrior2 = names

print(soldier1)
print(soldier2)
print(deceivers)
print(warrior1)
print(warrior2)
