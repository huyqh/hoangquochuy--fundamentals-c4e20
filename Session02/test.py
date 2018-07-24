yob = int(input("nhap vao nam sinh:"))
age = 2018 - yob
if age < 10:
    print("baby")
elif age < 18:
    print("teenage")
else:
     print("adult")