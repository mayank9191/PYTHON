# Write a recursive function to calculate the sum of first n natural numbers.
# n = 3
# sum = 1 + 2 + 3

# n = 6
# sum = 1 + 2 + 3 + 4 +5 +6

# n = n
# sum = 1 + 2 + 3 + . . . + (n-1) + n


def sum(n):

    if (n == 1):
        return 1

    return n + sum(n-1)


num = int(input("Enter positive number: "))
print(sum(num))
