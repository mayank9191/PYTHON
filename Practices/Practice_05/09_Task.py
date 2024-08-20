# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1, 2]}

print(s)

# ANSWER : No, you cannot have a list as an element of a set in Python. This is because lists are mutable and cannot be hashed, which is a requirement for elements of a set. Sets in Python can only contain immutable (hashable) types like integers, strings, tuples, etc.

s = {8, 7, 12, "Harry", (1, 2)}
print(s)

# Sets in Python can only contain immutable (hashable) like tuples in above ex
