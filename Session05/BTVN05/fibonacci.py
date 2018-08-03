# đệ quy.
n = int(input("how many months?"))
def F(n):
    if n == 0: return 1
    elif n == 1: return 2
    else: return F(n-1)+F(n-2)
print("month {} : {} pair(s) of rabbit".format(n,F(n)))


# khử đệ quy.
n = int(input("How many months?"))
a = 1
b = 2
sum = 0
for i in range(n+1):
    if i < 2:
        sum = i+1
    else:
        sum = a + b
        a = b
        b = sum
print("month {} : {} pair(s) of rabbit".format(n,sum))
