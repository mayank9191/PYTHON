# Write a program to print the following star pattern.
''' 
for n = 3
****
*  *
*  * 
****

'''

n = int(input("Enter no of level: "))

for i in range(1, n+1):
    if (i == 1 or i == n):
        print("* " * n)
    else:
        print("*", end="")
        print(" " * (2*n-3), end="")
        print("*")
