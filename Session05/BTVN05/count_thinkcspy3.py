string = "abcdefghijklmnopqrstuvyz"
print(string)
sentence = input("enter your sentence?").lower()
count = {}
for word in string:
    if word in sentence:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
keys = count.keys()
for word in sorted(keys):
    print(word,count[word])
