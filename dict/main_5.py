# %% A.15.5. Dictionary Mutability

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False
}

print(profile.get("affliations")[0].get("name"))

profile.get("affliations")[0]["name"] = "luigi steven"

print(profile.get("affliations")[0].get("name"))
