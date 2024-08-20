class Employee:
    language = "Python"  # This is a class atribute
    salary = 1200000


mayank = Employee()
mayank.name = "Mayank"  # This is a instance attribute
print(mayank.name, mayank.language, mayank.salary)

rohan = Employee()
rohan.name = "Rohan"   # This is a instance attribute
print(rohan.name, rohan.language, rohan.salary)

# Here name is object attribute and salary and language are object attributes as they directly belong to the class
