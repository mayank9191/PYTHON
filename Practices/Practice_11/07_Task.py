# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l
        print(f"Vector is {l[0]}i + {l[1]}j + {l[2]}k")

    def __add__(self, num):
        return f"{(self.a + num.a)}i + {(self.b + num.b)}j + {(self.c + num.c)}k"

    def __mul__(self, num):
        return f"{(self.a * num.a) + (self.b * num.b) + (self.c * num.c)}"

    def sum(n1, n2):
        print(f"Sum of Vectors = {n1 + n2}")

    def dot_product(n1, n2):
        print(f"Dot Product of Vectors = {n1 * n2}")

    def __len__(self):
        return len(self.l)


v1 = Vector([2, 5, 1])
print(len(v1))
