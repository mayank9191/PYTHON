# If the names of 2 friends are same; what will happen to the program in problem 6?

e = {}

n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e[n] = l

n = input("Enter your name : ")
l = input("Enter your favorite language : ")
e[n] = l

print(e)

# ANSWER : If the names of 2 friends are same only one is taken that comes last in dictionary
