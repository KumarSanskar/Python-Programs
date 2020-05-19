def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
res = hcf(a,b)
print("HCF of given two numbers",a,"and",b,"is: ",res)
