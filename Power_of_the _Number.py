# Program to find power for a given number using function pow
import math  # imports math module

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the value of power to the number: "))
res = math.pow(num1, num2)  # uses pow() function from Math module to find power
print(num1, "to the power", num2, "is", res)

# Program to find power of the given number without using any function

num = int(input("Enter the number: "))
power = int(input("Enter the value of power to the number: "))
sum = 1
i = 1
while i <= power:
    sum = sum * num
    i += 1
print(num, "to the power", power, "is", sum)

# Program to find power of the given number using ** method
num3 = int(input("Enter the number: "))
powr = int(input("Enter the value of power to the number: "))
result = num3**powr
print(num3,"to the power",powr,"is",result)

