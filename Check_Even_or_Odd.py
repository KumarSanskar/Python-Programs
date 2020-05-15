#  To check whether number is even or odd using modulus operator
num = int(input("Enter a number"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#  To check whether number is even or odd without using modulus operator
n = int(input("Enter a number"))
res = (n *2)/2
if res == n:
    print("Number is even")
else:
    print("Number is odd")

