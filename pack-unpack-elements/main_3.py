# %% A.46.3. Pemanfaatan teknik packing pada argument parameter

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
