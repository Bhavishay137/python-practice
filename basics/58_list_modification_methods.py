# Demonstrating common list modification methods in Python

a = []

# Adding a single element to the end of the list
a.append(10)
print("After append(10):", a)

# Inserting an element at a specific position
a.insert(0, 5)
print("After insert(0, 5):", a)

# Adding multiple elements to the list
a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

# Removing all elements from the list
a.clear()
print("After clear():", a)