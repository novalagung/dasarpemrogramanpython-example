# %% A.16.4. Nested dictionary

profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
    "affliations": [
        {
            "name": "luigi",
            "affliation": "brother"
        },
        {
            "name": "mushroom kingdom",
            "affliation": "protector"
        },
    ]
}

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])
print("affliations:")

for item in profile["affliations"]:
    print("  → %s (%s)" % (item["name"], item["affliation"]))

value = profile["affliations"][0]["name"], profile["affliations"][0]["affliation"]
print("  → %s (%s)" % (value))

value = profile["affliations"][1]["name"], profile["affliations"][1]["affliation"]
print("  → %s (%s)" % (value))
