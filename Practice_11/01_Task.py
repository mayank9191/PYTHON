# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y):
        print(f"x-coordinate = {x}\ny-coordinate = {y}")


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        print(f"z-coordinate = {z}")


x = Vector3D(2, 4, 6)
