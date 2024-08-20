# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Enter your Number: "))
myList = [num]

table = [num * item for item in range(1, 11)]

for i, item in enumerate(table, start=1):
    print(f"{num} X {i} = {item}")
