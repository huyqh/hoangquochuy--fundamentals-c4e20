# from random import choice
# word = "champion"
# list(word)
# for i in range(len(list(word))):
#     state = choice(list(word))
#     list = state
#     print(state)
#     list.remove(state)
from random import choice
word = "champion"
chars = list(word)
update_chars = []

loop = True
while loop:
    random_chars = choice(chars)
    update_chars.append(random_chars)
    chars.remove(random_chars)
    if len(chars)==0:
        loop = False
print(*update_chars)
ans = input("your guess:")
if ans == word:
    print("Hura")
else:
    print(":(")