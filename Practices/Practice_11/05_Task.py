# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(f"Vector is {a}i + {b}j + {c}k")

    def __add__(self, num):
        return f"{(self.a + num.a)}i + {(self.b + num.b)}j + {(self.c + num.c)}k"

    def __mul__(self, num):
        return f"{(self.a * num.a) + (self.b * num.b) + (self.c * num.c)}"

    def sum(n1, n2):
        print(f"Sum of Vectors = {n1 + n2}")

    def dot_product(n1, n2):
        print(f"Dot Product of Vectors = {n1 * n2}")


v1 = Vector(2, 5, 1)
v2 = Vector(3, 7, 5)

Vector.sum(v1, v2)
Vector.dot_product(v1, v2)
