# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter positive no: "))

mul = 1

if (num > 0):
    for i in range(1, num+1):
        mul *= i
    print(f"Factorial of a {num}! = {mul}")

elif (num == 0):
    print("Factorial of a 0! = 1")

else:
    print("Enter positive no only!")
