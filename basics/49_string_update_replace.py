# Program demonstrating string update and replace operation

s = "hello world"

# Update first character by creating a new string
s1 = "H" + s[1:]

# Replace a word in the string
s2 = s.replace("world", "Python")

print(s1)
print(s2)