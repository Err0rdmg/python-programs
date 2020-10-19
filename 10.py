s1 = input("Enter your 1st string:")
s2 = input("Enter your 2nd string:")
sp = input("Do you want space between them y/n:")
spa = sp.lower()

t = ""
l = ""
space = " "

for i in s1:
    if i.isupper():
        t += i

for i in s2:
    if i.islower():
        l += i

if spa == "y":
    print(t + space+l)
elif spa == "n":
    print(t+l)
else:
    print("There was an error please try again")
