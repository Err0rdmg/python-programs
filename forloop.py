a = input("Enter your text:")
alpha = input("Enter the letter you want to search:")


count = 0
for i in a:
    if i == alpha:
        count = count+1
print(count)
