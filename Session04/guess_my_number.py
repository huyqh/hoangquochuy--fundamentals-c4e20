
# print("think my number")
# input()

# ans = input("{} if my guess is {}maller than your number".format(s))
# ans = input("{} if my guess is {}maller than your number".format(l))



# low = 0
# high = 100
# mid = (low+high)/2

# for i in range(0,100):
#     if ans == "s":
#         high = mid



print("guess your number game?")
print("now thinhk of a number (0-100)")
input()
print("""
all you have to do is to answer to my guess
'c' if my guess is 'c'orrect
's' if my guess is 's'maller than your number
'l' if my guess is 'l'ager than your number
""")
low = 0
high = 100


playing = True
while playing:

    mid = (low + high)//2

    guess = input(" is {} your number:".format(mid))
    if guess == 'c':
        print("correct")
        playing = False
    elif guess == 's':
        low = mid
        print("smaller")
    else:
        high = mid
        print("larger")