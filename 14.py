s = input("Enter your string:")
le = 0
c_alpha = 0
c_digit = 0
c_sp = 0

for i in s:
    if i.isalpha:
        c_alpha += 1
    elif i.isnumeric:
        c_digit += 1
    elif i.isspace:
        c_sp += 1

print("Length of the string is:", len(s))

print("Number of alphabets is:", c_alpha)
print("Number of digits is:", c_digit)
print("Number of spaces is:", c_sp)
print("Number of words is:", c_sp+1)
print("Number of special symbols:", len(s) - (c_digit+c_sp+c_alpha))
