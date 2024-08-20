# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:

    def __init__(self, name, position, salary, increment):
        self.name = name
        self.position = position
        self.salary = salary
        self.new_salary = salary
        self.increment = int((increment*salary)/100)
        print(f"Employee_Name: {name}\nEmployee_Position: {
              position}\nEmployee_Salary: {salary}")

    @property
    def salaryAfterIncrement(self):
        return self.new_salary

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, num):
        self.new_salary = num + self.increment


name = input("Enter your name: ")
position = input("Enter your position: ")
salary = int(input("Enter your salary: "))
increment = int(input("Enter your increment percentage in salary: "))
e1 = Employee(name, position, salary, increment)
e1.salaryAfterIncrement = e1.salary
print(f"Incremented ammount: {e1.increment}")
print(f"Salary after increment: {e1.salaryAfterIncrement}")
