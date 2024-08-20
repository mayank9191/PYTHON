# Write a program to find the greatest of four numbers entered by the user.


a = int(input("Enter no 1 : "))
b = int(input("Enter no 2 : "))
c = int(input("Enter no 3 : "))
d = int(input("Enter no 4 : "))

# METHOD 1

if (a > b and a > c and a > d):
    largest = a
elif (b > c and b > d):
    largest = b
elif (c > d):
    largest = c
else:
    largest = d

print("Largest No is:", largest)


# ----------------------------------------------------------------------------

# METHOD 2

# if (a > b and a > c and a > d):
#     print("Largest No is : ", a)

# elif (b > c and b > d):
#     print("Largest No is : ", b)

# elif (c > d):
#     print("Largest No is : ", c)

# else:
#     print("Largest No is : ", d)

# -----------------------------------------------------------------------------

# METHOD 3

# l = []
# l.append(int(input("Enter no 1 : ")))
# l.append(int(input("Enter no 2 : ")))
# l.append(int(input("Enter no 3 : ")))
# l.append(int(input("Enter no 4 : ")))

# l.sort()
# print(l)
# print("Largest No is : ", l[-1])
