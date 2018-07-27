list = [5, 7, 300, 90, 24, 50, 75]
print("Hello, My name is Hiep and these are my sheep size:",list)
print("*"*100)



print("Now my biggest sheep has size {} let's shear it".format(max(list)))
print("*"*100)




for i in range(len(list)):
    if list[i] == max(list):
        list[i] = 8
        break
print("After shearing, here is my flock:",list)
print("*"*100)



for i in range(len(list)):
    list[i] += 50
print("one month has passed, now here is my flock:",list)
print("*"*100)



n = int(input("how many month?"))
for i in range(1,n+1):
    for j in range(len(list)):
        list[j] += 50
        
    print("one month has passed, now here is my flock:",list)
    print("now my biggest sheep has size {} let's shear it".format(max(list)))

    a = 0
    for i in range(len(list)):
        if list[i] > a:
            a = list[i]
            maxIndex = i
    
    list[maxIndex] = 8
    print("After shearing, here is my flock",list)
    print()
print("*"*100)



sum = sum(list)
money = sum*2
print("My flock has size in total: ", sum)
print("I would get ", sum, "* 2$ =", money,"$")