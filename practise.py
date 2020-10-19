lines = int(input("Enter number of lines you want:"))
astriks = int(input("Enter numbers of astriks per line you want:"))

for j in range(1, lines+1):
    for i in range(1, astriks+1):
        print("*", end="")
    print()

# print(""*lines)
# print("*"*astriks)
