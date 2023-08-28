# %% A.16.3. Perulangan data dictionary

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

for key in profile:
    print("key:", key, "\t value:", profile[key])
