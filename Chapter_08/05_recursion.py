def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Enter no: "))
print(f"The factorial of {n} is: {factorial(n)}")
