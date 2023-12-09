# %% A.31.2. Packing Element

soldier1 = 'Mikasa Ackerman'
soldier2 = 'Armin Arlert'
soldier3 = 'Eren Yeager'
warrior1 = 'Zeke Yeager'
warrior2 = 'Reiner Braun'
warrior3 = 'Annie Leonhart'

tuple1 = (soldier1, soldier2, soldier3, warrior1, warrior2, warrior3)
print(tuple1)

list1 = [soldier1, soldier2, soldier3, warrior1, warrior2, warrior3]
print(list1)

set1 = {soldier1, soldier2, soldier3, warrior1, warrior2, warrior3}
print(set1)

# %% ◉ Prepend element

names = [
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager',
    'Reiner Braun',
    'Annie Leonhart'
]

names = ('Jean Kirstein', *names)
print(f"type: {type(names).__name__}")

names2 = ['Jean Kirstein', *names]
print(f"type: {type(names2).__name__}")

names3 = {'Jean Kirstein', *names}
print(f"type: {type(names3).__name__}")

# %% ◉ Append element

names = [*names, 'Connie Springer']
print(names)

# %% ◉ Append dan prepend element bersamaan

names = {'Levi Ackerman', *names, 'Hange Zoë'}
print(names)
