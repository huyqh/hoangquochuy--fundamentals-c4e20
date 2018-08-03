# quy = ["Quy", 20, "Vinh Phuc", 2, 3, ["Anime", "ping pong"]]
# dictionary
# key : value
# create
person = {
    "name":"Quy",
    "age": 20,
    "university":"hust",
    "ex" : 2,
    "favs":["Anime", "ping pong"]
}
# read
# for key in person.keys():
#     print(key, end="\t")

# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)


person["gender"] = "male"
print(person)
# update
person["ex"] = 20
print(person)




# delete
del person["age"]
print(person)




key = "age"
if key in person:
    print(person[key])
else:
    print("not found")