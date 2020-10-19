s = input("Enter a string:")
t = ""

for i in s:
    if i == " ":
        t = t + '_'
    else:
        t = t+i
print(t)
