# Programs to check two no. are equal or not
n = int(input("Enter first no "))
p = int(input("Enter second no "))
if n == p:  # using equality operator and if else
    print("They are equal")
else:
    print("They are unequal")
print()
# Using ternary if else structure
# This will be printed at second time
print(" They are equal" if n == p else "They are unequal")
