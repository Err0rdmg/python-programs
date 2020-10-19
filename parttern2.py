lines = int(input("Enter number of lines:"))
space = lines-1

for i in range(lines+1):
    for j in range(0, space+1):
        print(" ", end="")
    for k in range(i, 1, -1):
        print(k, end="")
    for m in range(1, i+1):
        print(m, end="")
    space = space-1
    print()
