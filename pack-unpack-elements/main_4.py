# %% A.31.4. Packing-unpacking element dictionary

# %% ◉ Operasi unpack pada dictionary

data = {
    'id': 'U0001',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps',
    'gender': 'female'
}

user_id, *user_data = data
print(f"user_id: {user_id}")
print(f"user_data: {user_data}")

*user_data, gender = data
print(f"user_data: {user_data}")
print(f"gender: {gender}")

user_id, *user_data, gender = data
print(f"user_id: {user_id}")
print(f"user_data: {user_data}")
print(f"gender: {gender}")

# %% ◉ Operasi append & prepend pada dictionary

data = {
    'name': 'Mikasa Ackerman',
}
print(data)

data = {
    **data,
    'occupation': 'Paradise Survey Corps',
}
print(data)

data = {
    'id': 'U0001',
    **data,
    'gender': 'female',
}
print(data)

# %% ◉ Pemanfaatan teknik unpacking dictionary pada argument parameter

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
