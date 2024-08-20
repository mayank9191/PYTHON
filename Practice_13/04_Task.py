# Write a program to filter a list of numbers which are divisible by 5.

lists = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 34, 55, 100]


def divi(x):
    if (x % 5 == 0):
        return x


final = filter(divi, lists)
print(list(final))
