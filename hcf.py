
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

min = num1
if num2 < num1:
    min = num2

for i in range(1, min + 1):
    if((num1 % i) == 0 and (num2 % i) == 0):
        hcf = i

print("HCF of", num1, "and", num2, ":", hcf)
