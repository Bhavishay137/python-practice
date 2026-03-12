# Demonstrating different ways to remove elements from a list

a = [10, 20, 30, 40, 50]

# Remove a specific value from the list
a.remove(30)
print("After remove(30):", a)

# Remove element at index 1 and return it
popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

# Delete element using index
del a[0]
print("After del a[0]:", a)