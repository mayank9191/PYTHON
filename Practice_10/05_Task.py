# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    total_seat = 120

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("-----------------------------")
        print(f'''Welcome to Indian Railways\nThis is a booking for DELHI - MUMBAI Rajdhani Express\nPassenger Name: {
              self.name}\nAge: {self.age}''')

    def getStatus(self):
        print(f"Number of seats are: {Train.total_seat}")
        print("Price of 1 AC = ₹ 8045\nPrice of 2 AC = ₹ 4678\nPrice of 3 AC = ₹ 1598\nPrice of Sleeper = ₹ 997")

    def book(self, num):
        if (Train.total_seat > 0):
            Train.total_seat = Train.total_seat - 1
            if (num == 1):
                print(
                    "Your seat got confirmed in 1 AC and default birth is lower(want to change login again)")
            elif (num == 2):
                print(
                    "Your seat got confirmed in 2 AC and default birth is lower(want to change login again)")
            elif (num == 3):
                print(
                    "Your seat got confirmed in 3 AC and default birth is lower(want to change login again)")
            elif (num == 4):
                print(
                    "Your seat got confirmed in Sleeper and default birth is lower(want to change login again)")
            else:
                print("Select valid Class Number")
        else:
            print("Sorry, all seats are booked")


name = input("Enter your Name here: ")
age = input("Enter your age here: ")
p1 = Train(name, age)
p1.getStatus()
num = int(input("Select Class (1 AC, 2 AC, 3 AC, Sleeper) to book as (1, 2, 3, 4): "))
p1.book(num)

name = input("Enter your Name here: ")
age = int(input("Enter your age here: "))
p2 = Train(name, age)
p2.getStatus()
num = int(input("Select Class (1 AC, 2 AC, 3 AC, Sleeper) to book as (1, 2, 3, 4): "))
p2.book(num)

name = input("Enter your Name here: ")
age = int(input("Enter your age here: "))
p3 = Train(name, age)
p3.getStatus()
num = int(input("Select Class (1 AC, 2 AC, 3 AC, Sleeper) to book as (1, 2, 3, 4): "))
p2.book(num)
