class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language {self.language}.The salary is {self.salary}")

    # donot requires object properties(not requires self statement)
    @staticmethod
    def greet():
        print("Good Morning!")


mayank = Employee()
mayank.language = "Javascript"
mayank.getInfo()
mayank.greet()

# it automatically converts into Employee.getInfo(mayank) so we have to use self as an argument in method function in class
