#  progrm to print fibbonaci series i.e. 1,1,2,3,5,8(a series in which in which a number is sum of two preceding terms)
a = 0  # setting the first term as zero
b = 1  #setting second term as one
num = int(input("Enter number for how many times series is to be generated: "))
print("The given fibbonaci series for",num,"terms is:")
print("",b,end = "")
for i in range(num):
    c = a + b  # making third term as sum of first two terms
    a = b  # interchanging the second term as to first term
    b = c  # interchanging third term as to second term
    print(" ",c,end ="")