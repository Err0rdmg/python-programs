st = input("Enter your string: ")
t = ""

for i in st:
    if i in "AEIOUaeiou":
        t += '*'
    else:
        t += i

print(t)
