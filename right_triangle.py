line = int(input("Enter numbers of lines you want:"))
# astriks = int(input("Enter numbers of astriks per line you want:"))


for i in range(line, 0, -1):
    if i == 1 or i == line:
        for j in range(1, i+1):
            print("*", end="")
    else:
        for j in range(1, i+1):
            if j == 1:
                print("*", end="")
            else:
                print(" ", end="")

    print()
