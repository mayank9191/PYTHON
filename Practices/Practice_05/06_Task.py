# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

e = {}

# n = input("Enter your name : ")
# l = input("Enter your favorite language : ")
# e[n] = l


n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e.update({n: l})

n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e.update({n: l})

n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e.update({n: l})

n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e.update({n: l})


print(e)
