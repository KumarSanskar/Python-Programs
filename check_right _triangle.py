# check whether the triangle is right angled or not using Hypotenuse perpendicular and base as parameters
h = int(input("Enter length of Hypotenuse "))
p = int(input("Enter length of Perpendicular "))
b = int(input("Enter length of Base "))
if h ** 2 == p ** 2 + b ** 2:                    # from Pythagoras Theorem(h^2=p^2+b^2)
    print("Triangle is right angled")
else:
    print("Triangle is not right angled")
