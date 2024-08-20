# Add a static method in problem 2, to greet the user with hello.

import math


class Calculator:

    @staticmethod
    def greet():
        print("Hello little Mathematician ")

    def __init__(self, num):
        self.num = num
        print(f"Square of {num} = {num*num}\nCube of {num} = {num *
              num*num}\nSquare Root of {num} = {math.sqrt(num)} ")


num = int(input("Enter your number: "))

n = Calculator(num)
