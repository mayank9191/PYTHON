# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, gender, language, department):
        print("Hi Microsoftian! your data has been taken")
        self.name = name
        self.gender = gender
        self.language = language
        self.department = department

    def getInfo(self):
        print(f'''Name: {self.name}\nGender: {self.gender}\nLanguage: {
              self.language}\nDepartment: {self.department}''')


name = input("Enter your name: ")

gender = input("Enter your gender: ")

language = input("Enter your language: ")

department = input("Enter your department: ")

Employee1 = Programmer(name, gender, language, department)

print("Your details are:")
Employee1.getInfo()
