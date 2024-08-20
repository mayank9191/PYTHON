# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass


class Pets(Animals):
    def __init__(self):
        print("These are those animal which can be kept with human")


class Dog(Pets):
    def __init__(self):
        super().__init__()

    def Bark(self):
        print("Baw Baw Baw!!!!!")


o = Dog()
o.Bark()
