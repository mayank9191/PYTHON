class Employee:
    company1 = "ITC"

    name = "Mayank"

    def show(self):
        print(f"Name is {self.name} and company is {self.company1}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages here is your language: {
              self.language}")


class Programmer(Employee, Coder):

    company2 = "ITC infotech"

    def showLanguage(self):
        print(f"Name is {self.company2} and he is good with {
            self.language} language")


b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()
