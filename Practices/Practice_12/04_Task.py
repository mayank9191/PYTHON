# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter vlaue of a: "))
    b = int(input("Enter vlaue of b: "))

    print(f"Result = {round(a/b, 2)}")


except ZeroDivisionError:
    print("Result = \u221E")

except ValueError:
    print("Please enter valid integers for a and b")
