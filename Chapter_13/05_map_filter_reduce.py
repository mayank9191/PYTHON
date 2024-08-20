from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]
def square(x): return x*x


# it creates a list containing element output of function enterd in map
sqList = map(square, l)
print(list(sqList))

# Filter Example


def even(n):
    if (n % 2 == 0):
        return True
    return False


# it will filter out with function
onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example


def sum(a, b): return a+b


def mul(x, y): return x*y


# it reduce a list by function and give output
print(reduce(sum, l))
print(reduce(mul, l))
