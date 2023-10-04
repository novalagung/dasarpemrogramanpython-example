# %% A.23.2. Keyword argument

def create_sorcerer(name, age, race, era):
    return {
        "name": name,
        "age": age,
        "race": race,
        "era": era,
    }

obj5 = create_sorcerer("Sukuna", 1000, "incarnation", "heian")
print(obj5)

obj6 = create_sorcerer(name="Kenjaku", age=1000, race="human", era="1000+ year ago")
print(obj6)

obj7 = create_sorcerer("Hajime Kashimo", 400, race="human", era="400 year ago")
print(obj7)

obj8 = create_sorcerer(era="1000+ year ago", age=1000, name="Kenjaku", race="human")
print(obj8)

obj9 = create_sorcerer("Hajime Kashimo", 400, era="400 year ago", race="human")
print(obj9)
