# Write a program to print the content of a list using while loops.

lists = []
num = int(input("Enter number of list item to add: "))
i = 0

while (i < num):
    lists.append(input(f"Enter item no. {i} to add in list: "))
    i += 1

i = 0

while (i < num):
    print(f"List item no.{i}:", lists[i])
    i += 1
