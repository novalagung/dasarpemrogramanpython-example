# A.52.1. Implementasi JSON di Python

# %% ◉ Encode data Python ke JSON string

import json

data = {
    'name': 'Maiev Shadowsong',
    'affliations': ['Warden', 'Alliance']
}
jstr = json.dumps(data)
print(jstr)

# %%

import json

data = [
    {
        'faction': 'Horde',
        'color': 'red',
        'founding_members': [
            'Orc',
            'Undead',
            'Tauren',
            'Troll',
            'Blood Elf',
            'Goblin'
        ],
        'total_members': 13,
        'active': True,
    },
    {
        'faction': 'Alliance',
        'color': 'blue',
        'founding_members': [
            'Human',
            'Dwarf',
            'Night Elf',
            'Gnome',
            'Draenei',
            'Worgen'
        ],
        'total_members': 13,
        'active': True,
    }
]
jstr = json.dumps(data, indent=4)
print(jstr)

# %%

import json

data = [
    {
        'colors': {'black', 'white'},
    }
]
jstr = json.dumps(data)
print(jstr)
