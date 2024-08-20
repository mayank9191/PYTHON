a = 32
t = type(a)  # it will tell the type of variable
print(t)

b = type(t)  # it tells that b is a type variable telling a type <int>
print(b)

c = "mayank"
d = type(c)
print(d)

e = 76.23
print(type(e))

f = True
print(type(f))

# Conversion

a = "25.5"  # As a is str but converted into float b
b = float(a)
print(type(a))
print(type(b))
