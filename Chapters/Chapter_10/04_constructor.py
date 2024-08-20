class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, language, salary):  # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")


mayank = Employee("Mayank", "Javascript", 1200000)
print(mayank.name, mayank.language, mayank.salary)
