space = 0
for i in range(5, 0, -1):
    for k in range(1, space + 1):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end="")
    print()
