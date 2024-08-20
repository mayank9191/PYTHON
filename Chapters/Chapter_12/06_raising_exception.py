a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# We can raise custom exceptions using the ‘raise’ keyword in python.

if (b == 0):
    raise ZeroDivisionError(
        "Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")
