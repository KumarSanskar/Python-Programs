# to create a list of even and no in list between 1 to 100
ls1 = []        # creation of two lists
ls2 = []
for i in range(1, 100):             # use of for loop in range 1 to 100
    if i % 2 == 0:                  # checks for the condition whether the no is even
        ls1.append(i)
    else:                                   # appends the no to ls1 if even else to ls2
        ls2.append(i)
i = i+1                                     # increases the value after evaluation
print("list of even no is as follows: ", ls1)
print("list of odd no is as follows: ", ls2)
