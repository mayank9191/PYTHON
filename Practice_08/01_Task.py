# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if (a > b and a > c):
        print(f"{a} is greatest among three")

    elif (b > c):
        print(f"{b} is greatest among three")

    else:
        print(f"{c} is greatest among three")


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print(max(a, b, c))
