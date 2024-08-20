# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Test:
    a = 1   # This is a class attribute


object = Test()
print(object.a)
object.a = 0  # This is instance attribute which have higher priority over class attribute
print(object.a)
