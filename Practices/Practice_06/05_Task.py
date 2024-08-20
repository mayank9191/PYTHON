# Write a program which finds out whether a given name is present in a list or not.

lists = []

lists.append(input("Enter name to add in list : "))
lists.append(input("Enter name to add in list : "))
lists.append(input("Enter name to add in list : "))
lists.append(input("Enter name to add in list : "))

find = input("Enter name to find out from list : ")

# METHOD 1

if (find in lists):
    print("Given name is not present in a list")

else:
    print("Given name is present in a list")


# METHOD 2

# if (lists.count(find) == 0):
#     print("Given name is not present in a list")

# else:
#     print("Given name is present in a list")
