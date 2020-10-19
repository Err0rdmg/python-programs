msg = input("Enter your string:")
msg1 = ''

for i in range(0, len(msg)):
    if msg[i].isupper():
        msg1 += msg[i].lower()
    elif i % 2 == 0:
        msg1 += '*'
    else:
        msg1 += msg[i].upper()
print(msg1)
