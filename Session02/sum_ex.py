n = int(input("Nhap vao gia tri n:"))
sum = 0
for i in range(0,n+1,1):
    sum = sum + i
print(sum)




n = int(input("nhap vao gia tri cua n:"))
sum = n*(n+1)/2
print(sum)




n = int(input("nhap vao gia tri cua n:"))
i = range(n+1)
b = sum(i)
print(b)
