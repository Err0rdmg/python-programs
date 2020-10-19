str = input("Enter your string:")
count = 0

for i in str:
    if i.islower():
        count += 1
print("Your string have", count, "lowercase letters")
