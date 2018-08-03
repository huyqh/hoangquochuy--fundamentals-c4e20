inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}


# add key
inventory["pocket"] = ["seashell", "strange berry", "lint"]

# delete
del(inventory["backpack"][1])

# update
inventory["gold"] = 50
print(inventory)

