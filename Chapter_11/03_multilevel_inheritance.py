class Employee:
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3


p1 = Employee()
print(p1.a)  # prints the a attribute
print(p1.b)  # shows an error as there is no b attribute in Employee class

p1 = Programmer()
print(p1.a, p1.b)

p1 = Manager()
print(p1.a, p1.b, p1.c)
