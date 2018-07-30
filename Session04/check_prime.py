numb = int(input("n?"))
is_prime = True

i = 2
while i<numb:
    if numb % i == 0:
        is_prime = False
    i += 1
if is_prime:
    
    print("{} is a prime number".format(numb))
else:
    print("not")