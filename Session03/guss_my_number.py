from random import randint
numb = randint(0,100)
playing = True
guess = int(input("Guess my number:"))
while playing:
    if guess > numb:
        print("a little too large")
    elif guess < numb:
        print("too small")
    else: 
        print("Bingo")
        break
    count = 0
    count += 1
    if count == 8:
        print("You lose")
    playing = False