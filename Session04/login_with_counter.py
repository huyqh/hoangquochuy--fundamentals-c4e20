username = input("username:")
password = input("password")

count = 0
loop = True
while loop:
    if username == "c4e":
        if password == "codethechange":
            print("yes")
            break
        else:
            print("no")
            loop = False
    else:
        print("no")
    count += 1
    if count == 3:
        loop = False