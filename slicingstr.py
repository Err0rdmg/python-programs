str = "Hello, World!"

#str[start: stop:step]

# slicing str
print("Basic slicing")
print("1", str[1:])
print("2", str[:5])
print("3", str[6:10])
print("4", str[-12:-6])

# step string slicing
print("Step string slicing")
print("1", str[:12:2])

# reverse slicing
print("Reverse slicing")
print("1", str[::-1])
