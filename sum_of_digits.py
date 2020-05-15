#  This program calculates the sum of digits of an input number
num = int((input("Enter the number: ")))  # takes input from user in integer format
sum = 0
while num > 0:  # iterates till value of num becomes zero
    x = num%10
    sum =sum + x
    num = num//10
print("sum of digits is ",sum)
