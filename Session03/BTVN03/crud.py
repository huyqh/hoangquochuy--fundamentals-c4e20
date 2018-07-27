menu = ["T-Shirt","Sweater"]
running = True
while running:
    choose = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if choose == "R":
        for index, item in enumerate(menu):
            print(" Our shop have: {},{}".format(index+1,item))
    print("*"*20)

    if choose == "C":
        new_update = input("Enter new item:")
        menu.append(new_update)
        for index, item in enumerate(menu):
            print("Our items:{},{}".format(index+1,item))
    print("*"*20)

    if choose == "U":
        pos_update = int(input("update position?"))
        menu[pos_update-1] = "Skirt"
        for index, item in enumerate(menu):
            print("Our items:{},{}".format(index+1,item))
    print("*"*20)

    if choose == "D":
        pos_delete = int(input("delete position?"))
        pos_delete = menu[pos_delete-1]
        menu.remove(pos_delete)
        for index, item in enumerate(menu):
            print("Our items:{},{}".format(index+1,item))
    print("*"*20)
running = False

