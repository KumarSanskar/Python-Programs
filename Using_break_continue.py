# Program showing the use of break and continue statement simultaneously
while True:
    val = input("Enter a Number")
    if val == "q":
        print("Exiting from the program as you entered a special key ")

    if not val.isdigit():
        print("Enter digits only, continue statement will be used now!!!")
    continue
    val =int(val)
    print(val**3)