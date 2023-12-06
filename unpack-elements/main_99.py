# %%

names = ('Mikasa Ackerman', 'Armin Arlert', 'Eren Yeager', 'Zeke Yeager', 'Reiner Braun', 'Annie Leonhart')

soldier1, soldier2, soldier3, warrior1, warrior2, warrior3 = names

print(soldier1)
print(soldier2)
print(soldier3)

print(warrior1)
print(warrior2)
print(warrior3)

# %%

names = ('Mikasa Ackerman', 'Armin Arlert', 'Eren Yeager', 'Zeke Yeager', 'Reiner Braun', 'Annie Leonhart')

soldier1, soldier2, deceiver1, *warriors = names

print(soldier1)
print(soldier2)
print(deceiver1)
print(warriors)

# %%

names = ('Mikasa Ackerman', 'Armin Arlert', 'Eren Yeager', 'Zeke Yeager', 'Reiner Braun', 'Annie Leonhart')

*soldiers, deceiver1, deceiver2, warrior1, warrior2 = names

print(soldiers)
print(deceiver1)
print(deceiver2)
print(warrior1)
print(warrior2)

# %%

names = ('Mikasa Ackerman', 'Armin Arlert', 'Eren Yeager', 'Zeke Yeager', 'Reiner Braun', 'Annie Leonhart')

soldier1, soldier2, *deceivers, warrior1, warrior2 = names

print(soldier1)
print(soldier2)
print(deceivers)
print(warrior1)
print(warrior2)

# %%

names = ('Jean Kirstein', *names)
print(names)

# %%

names = (*names, 'Connie Springer')
print(names)

# %%

names = ('Levi Ackerman', *names, 'Hange Zoë')
print(names)

# %%

def show_biography(id, name, occupation, gender):
    print(f"id: {id}")
    print(f"name: {name}")
    print(f"occupation: {occupation}")
    print(f"gender: {gender}")

id = 'U0001'
name = 'Mikasa Ackerman'
occupation = 'Paradise Survey Corps'
gender = 'female'
show_biography(id, name, occupation, gender)

user2_id = 'U0002'
user2_data = ('Annie Leonhart', 'Marley Warrior', 'female')
show_biography(user2_id, *user2_data)

user3_data = ('U0003', 'Levi Ackerman', 'Paradise Survey Corps')
show_biography(*user3_data, 'male')

user4_data = ('Hange Zoë', 'Paradise Survey Corps')
show_biography('U0004', *user4_data, 'male')

# %%

data = {
    'id': 'U0001',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
}
data = {
    **data,
    'gender': 'female',
}
print(data)

user_id, *user_data = data
print(user_id, user_data)

*user_data, gender = data
print(user_data, gender)

user_id, *user_data, gender = data
print(user_id, user_data, gender)

# %%

def show_biography(id, name, occupation, gender):
    print(f"id: {id}")
    print(f"name: {name}")
    print(f"occupation: {occupation}")
    print(f"gender: {gender}")

data1 = {
    'id': 'U0001',
    'gender': 'female',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
}
show_biography(**data1)

data2 = {
    'gender': 'female',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
}
show_biography('U0002', **data2)
