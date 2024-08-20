# Write __str__() method to print the vector as follows: 7i + 8j +10k

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"


v1 = Vector(7, 8, 10)
print(v1)
