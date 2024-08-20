# Write a python function which converts inches to cms.(modified)

def convertor1(num):
    print(num * 2.5, "cm")


def convertor2(num):
    print(num / 2.5, "inches")


def convertor3(num):
    print(int(num/30), "feet")


print("Length Covertor\ninches -> cm (press 1)\ncm - >inches (press 2)\ncm -> feet (press 3)")
a = int(input("Enter your choice here: "))


if (a == 1):
    n = int(input("Enter length in inches: "))
    convertor1(n)

elif (a == 2):
    n = int(input("Enter length in cm: "))
    convertor2(n)

elif (a == 3):
    n = int(input("Enter length in cm: "))
    convertor3(n)

else:
    print("Please choose valid choice")
