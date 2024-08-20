# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Enter your Number: "))
myList = [num]

table = [num * item for item in range(1, 11)]


with open("Practice_12/Tables.txt", "a") as f:
    for i, item in enumerate(table, start=1):
        f.write(f"{num} X {i} = {item}\n")

print(f"Table of {num} is printed in Tables.txt ")
