str = input("Enter your string:")
t = ""

for i in str:
    if i.isupper():
        t += i.lower()
    elif i.islower():
        t += i.upper()
    else:
        t += i
print("Your final string is:", t)
