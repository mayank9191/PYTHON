# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

'''
n1
n2
.
.
.
'''

num = int(input("Enter number: "))
lists = [str(i*num) for i in range(1, 11)]
final = "\n".join(lists)
print(final)
