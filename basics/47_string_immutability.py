# Program demonstrating string immutability in Python

s = "python and learn"

# Create a new string because strings cannot be modified directly
s = "G" + s[1:]

print(s)