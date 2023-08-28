# %% A.15.2. Pembuatan dictionary

profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}
print(profile)

profile = dict(
    set= "id",
    name= "john wick",
    hobbies= ["playing with pencil"],
    is_female= False,
)
print(profile)

profile = dict([
    ('set', "id"),
    ('name', "john wick"),
    ('hobbies', ["playing with pencil"]),
    ('is_female', False)
])
print(profile)

profile = dict()
print(profile)

profile = {}
print(profile)
