# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, a, b):
        self.real_part = a
        self.imaginary_part = b
        print(f"Your Complex Number: {a} + {b}i")

    def __add__(self, num):
        return f"c1 + c2 = {self.real_part + num.real_part} + {self.imaginary_part + num.imaginary_part}i "

    def __mul__(self, num):
        return f"c1 * c2 = {(self.real_part*num.real_part) - (self.imaginary_part * num.imaginary_part)} + {(self.real_part*num.imaginary_part) + (num.real_part*self.imaginary_part)}i"

    def Add(self, new):
        print(self + new)

    def Multiply(self, new):
        print(self * new)


a = int(input("Enter real part of c1: "))
b = int(input("Enter imaginary part of c1: "))
c1 = Complex(a, b)

c = int(input("Enter real part of c2: "))
d = int(input("Enter imaginary part of c2: "))
c2 = Complex(c, d)

Complex.Add(c1, c2)
Complex.Multiply(c1, c2)
