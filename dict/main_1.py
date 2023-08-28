# %% A.15.1. Penerapan dictionary

profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

print(profile)
print("total keys:", len(profile))

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])

# %% ◉ Pretty print dictionary

import pprint
pprint.pprint(profile)

import json
print(json.dumps(profile, indent=4))
