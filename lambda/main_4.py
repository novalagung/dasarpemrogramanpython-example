# %% A.26.4. Lambda *args dan **kwargs

def debug1(separator, *params):
    res = []
    for i in range(len(params)):
        res.append(f"param {i}: {params[i]}")
    return separator.join(res)

debug2 = lambda separator, *params : separator.join([f"param {i}: {params[i]}" for i in range(len(params))])

res = debug1(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)

res = debug2(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True)
print(res)

# %%

def debug3(separator, **params):
    res = []
    for key in params:
        res.append(f"{key}: {params[key]}")
    return separator.join(res)

debug4 = lambda separator, **params : separator.join([f"{key}: {params[key]}" for key in params])

res = debug3(
    ", ",
    name="Darion Mograine",
    occupations=["Highlord", "Horseman of the Ebon Blade", "Ashbringer"],
    active=True
)
print(res)

res = debug4(
    ", ",
    name="Darion Mograine",
    occupations=["Highlord", "Horseman of the Ebon Blade", "Ashbringer"],
    active=True
)
print(res)
