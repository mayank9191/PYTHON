class Employee:
    company1 = "ITC"
    language = "Python"
    name = "Mayank"

    def show(self):
        print(f"Name is {self.name} and company is {self.company1}")


# class Programmer():
#     company = "ITC infotech"

#     def show(self):
#         print(f"Name is {self.name} and salary is {self.salary}")

#     def showLanguage(self):
#         print(f"Name is {self.name} and he is good with {
#               self.language} language")

class Programmer(Employee):

    company2 = "ITC infotech"

    def showLanguage(self):
        print(f"Name is {self.company2} and he is good with {
            self.language} language")


b = Programmer()

b.show()
b.showLanguage()
