#  Nested if example(using parameter of number should be greater than 30):
num = int(input("Enter a number greater than 30"))
if num >= 30:
    print("Number accepted")
    if num % 2 == 0:
        print("Number is even")
else:
    print("Number is smaller than 30, please re-enter")