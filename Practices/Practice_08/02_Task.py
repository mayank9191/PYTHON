# Write a python program using function to convert Celsius to Fahrenheit(modified temperature convertor).

print("Temperature convertor\nFor Celsius -> Fahrenheit press 1\nFor Fahrenheit -> Celsius press 2\nFor Celsius -> Kelvin press 3")
a = int(input("Select: "))


def temp_convertor1(temp):
    c = temp * (9/5) + 32
    print(round(c, 2), "°F")


def temp_convertor2(temp):
    c = (temp - 32) * (5/9)
    print(round(c, 2), "°C")


def temp_convertor3(temp):
    print(temp + 273.15, "K")


if (a == 1):
    c = float(input("Enter temperature in celsius: "))
    temp_convertor1(c)


elif (a == 2):
    c = float(input("Enter temperature in fahrenheit: "))
    temp_convertor2(c)


elif (a == 3):
    c = float(input("Enter temperature in celsius: "))
    temp_convertor3(c)


else:
    print("please enter a valid choice.")
