class Employee:
    language = "Python"  # This is a class aattribute
    salary = 1200000


mayank = Employee()

mayank.language = "Javascript"  # This is an instance attribute
print(mayank.language, mayank.salary)

# Instance attributes, take preference over class attributes during assignment & retrieval.
