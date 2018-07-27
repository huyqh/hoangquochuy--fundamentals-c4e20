n = int(input("Nhap vao gia tri cua n:"))

# counting = True
# count = 0
# while counting :
#     n = n // 10
#     count += 1
#     if n == 0:
#         counting = False
# print(count)        
count = 0
while n != 0:
    n = n // 10
    count += 1
print(count)