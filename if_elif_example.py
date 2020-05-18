#  If....elif example(using program to tell grade of a student according to percentage)
percen = int(input("Enter  your percentage: "))
if percen > 95:
    print("Your grade is A+")
elif percen >85 and percen< 95:
    print("Your grade is B+")
elif percen > 80 and percen< 85:
    print("Your grade is B")
elif percen > 75 and percen< 80:
    print("Your grade is C+")
elif percen > 70 and percen< 75:
    print("Your grade is C")
else:
    print("You have failed.")