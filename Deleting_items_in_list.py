#  Using various methods to delete items from list:

#  Using ***.remove() method:
lst1 = ["Ram", "Shyam", "Ghanshayam"]
print("list before removing: ", lst1)
lst1.remove("Ram")
print("list after removing: ",lst1)

#  Using ***.pop() method to remove item from the list:
lst1 = ["Ram", "Shyam", "Ghanshayam"]
print("list before using .pop: ", lst1)
lst1.pop()  # this will remove the last elemnt as index is not specified
print("list after using .pop(): ", lst1)
lst1.pop(0)  # this will remove the tem from the index 0
print("list after using .pop(0): ", lst1)

# Using del() :
lst1 = ["Ram", "Shyam", "Ghanshayam"]
print("List before using del(): ",lst1)
del lst1[0]  # is used to delete at specified index
print("List after using del ", lst1)

# Using ***.clear() , it removes everything from the list
lst1 = ["Ram", "Shyam", "Ghanshayam"]
print("List before using .clear(): ", lst1)
lst1.clear()  # this will empty the elements of the list
print("List after using .clear(): ",lst1)

# Using del keyword to delete entire list:
lst1 = ["Ram", "Shyam", "Ghanshayam"]
print("List before using del keyword is: ", lst1)
del lst1  # this will delete the entire list
print("The list is:",lst1)
