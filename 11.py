s = input("Enter your string:")

t = s.replace(s[0], "$")
r = s[0]+t[1:]

print(r)
