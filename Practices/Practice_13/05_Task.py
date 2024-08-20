# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [2, 3, 426, 66, 78, 1, 43, 47, 800]


def max(x, y):
    if (x > y):
        return x
    else:
        return y


final = reduce(max, l)
print(f"Maximum of the numbers in a list is {final}")
