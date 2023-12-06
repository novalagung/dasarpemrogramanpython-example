# %% A.16.6. Operasi data dictionary

# %% ◉ Pengaksesan item

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print("id:", profile["id"])
print("name:", profile.get("name"))

# %% ◉ Mengubah isi dictionary

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}
print("name:", profile["name"])

profile["name"] = "mario mario"
print("name:", profile["name"])

# %% ◉ Menambah item dictionary

profile = {
    "name": "mario",
}
print("len:", len(profile), "data:", profile)

profile["favourite_color"] = "red"
print("len:", len(profile), "data:", profile)

profile.update({"race": "italian"})
print("len:", len(profile), "data:", profile)

# %% ◉ Menghapus item dictionary

profile.pop("hobbies")
print(profile)

del profile["id"]
print(profile)

# %% ◉ Pengaksesan dictionary keys

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print(list(profile.keys()))

# %% ◉ Pengaksesan dictionary

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print(list(profile.values()))

# %% ◉ Method `items()` dictionary

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print(list(profile.items()))

# %% ◉ Copy dictionary

p1 = {
    "id": 2,
    "name": "mario",
    "is_female": False,
}
print(p1)

p2 = p1.copy()
print(p2)

# %% ◉ Mengosongkan isi dictionary

profile = {
    "id": 2,
    "name": "mario",
    "is_female": False,
}
print("len:", len(profile), "data:", profile)

profile.clear()
print("len:", len(profile), "data:", profile)
