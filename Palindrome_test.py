# program to check that given string is palindrome or not(case-sensitive)
a = str(input("Enter the string to be checked: "))
if a == a[::-1]:
    print("It's a palindrome string.")
else:
    print("No, It's not a palindrome.")
