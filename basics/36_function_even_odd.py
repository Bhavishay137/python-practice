# Program to check whether a number is even or odd using a function

def evenOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))