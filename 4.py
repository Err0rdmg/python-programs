text = input("Enter your string:")

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i], end=" ")

        # or

for i in range(0, len(text), 2):
    print(text[i], end="")
