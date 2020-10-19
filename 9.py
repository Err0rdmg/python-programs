str = input("Enter your string:")
t = ""

for i in range(0, len(str)):
    if i % 2 == 0:
        t += str[i].lower()
    else:
        t += str[i].upper()
print(t)
