# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”


name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phoneNumber = int(input("Enter your phone number: "))

print("Name of the student is {}, his marks are {} in Mathematics and phone number is {}".format(
    name, marks, phoneNumber))
