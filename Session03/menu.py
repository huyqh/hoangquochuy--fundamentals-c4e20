# list/ array
# create
menu = ["com","ca","thit bo"]
# seperator
print(*menu, sep=", ")
menu.append("ghe")
print(*menu,sep=", ")
# length
size = len(menu)
print(len(menu))
# indexing
print(menu[0])
# for i in range(len(menu)):
#     print(menu[i])
for index, item in enumerate(menu):
    print(index +1 ,item, sep = ", ")
# for item in menu:
#      print(item)
for index, item in enumerate(menu):
    print("{},{}".format(index+1,item))
# update
menu[2] = "tom hum"
print(*menu,sep=", ")

