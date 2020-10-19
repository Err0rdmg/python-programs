x = input("Enter your string:")
y = x.lower()

count = 0

for i in y:
    # if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    # or
    if i in "aieou":
        count += 1

print("Number of vowels in your string is", count)
