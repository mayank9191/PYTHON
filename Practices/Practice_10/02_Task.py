# Write a class “Calculator” capable of finding square, cube and square root of a number.

import math


class Calculator:
    def __init__(self, num):
        self.num = num
        print(f"Square of {num} = {(num)**2}\nCube of {num} = {(num)
              ** 3}\nSquare Root of {num} = {math.sqrt(num)}")


num = int(input("Enter your number: "))
n = Calculator(num)
