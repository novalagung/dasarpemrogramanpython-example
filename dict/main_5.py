# %% A.16.5. Dictionary Mutability

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False
}

print(profile["affliations"][0]["name"])

profile["affliations"][0]["name"] = "luigi steven"

print(profile["affliations"][0]["name"])
