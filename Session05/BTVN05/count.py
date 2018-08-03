# with count()
list = [1, 6, 8, 1, 2, 1, 5, 6]
print(list)
n = int(input("enter your number?"))
x = list.count(n)
print("{} appears {} times in list".format(n,x))



# without count()
list = [1, 6, 8, 1, 2, 1, 5, 6]
print(list)
n = int(input("enter your number?"))
count = 0
for i in range(len(list)):
    if list[i] == n:
        count += 1
print("{} appears {} times in list".format(n,count))