teen_code = {"hc": "hoc", "ng": "nguoi", "pt": "phat trien", "eny":"em nguoi yeu", "any":"anh nguoi yeu",
"ns": "noi", "ngta":"nguoi ta", "lm":"lam","r":"roi", "stt":"status"}

loop = True
while loop:


    for key in teen_code.keys():
        print(key,end ="\t")
    key = input("Your code?")
    if key in teen_code:
        print(teen_code[key])
    else:
        print("not found, do you want to contribute this word?(Y/N)?")
        add = input("Y/N?")
        if add == "Y":
            word = input("enter your word:")
            translate = input("enter your translate:")
            teen_code[word] = translate
            print(teen_code)
        else:
            print()
    loop = False






teencode = {"hc": "hoc", "ng": "nguoi", "pt": "phat trien", "eny":"em nguoi yeu", "any":"anh nguoi yeu",
"ns": "noi", "ngta":"nguoi ta", "lm":"lam","r":"roi", "stt":"status"}
loop = True
while loop:
    for key in teencode.keys():
        print(key, end="\t")
    code = input("Your code?")
    print("*"*100)
    if code in teencode:
        print("translate:",teencode[code])
    else:
        contribute = input("not found, do you want to contribute this word? (Y?N) ").upper()
        if contribute == "Y":
            trans = input("translation:")
            teencode[code] = trans
            print("updated")
        else:
            False
    print("*"*100)
