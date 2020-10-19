line = int(input("Enter numbers of lines you want:"))
astriks = int(input("Enter numbers of astriks per line you want:"))

for i in range(1, line+1):
    if i == 1 or i == line:
        for j in range(1, astriks + 1):
            print("*", end="")
    else:
        print("*", " " * (line-2), "*", sep="", end="")
    print()
