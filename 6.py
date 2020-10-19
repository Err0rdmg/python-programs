t = input("Enter your text:")
j = 1
for i in range(0, len(t)):
    for a in range(0, i+1):
        print(t[a], end="")
    print()
