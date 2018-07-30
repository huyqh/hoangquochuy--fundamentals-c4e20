name = input("Your full name:")
new_name = name.lower()
list = new_name.split()
print("updated:", str.join(" ", list).title())
