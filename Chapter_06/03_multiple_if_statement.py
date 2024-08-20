a = int(input("Enter your age : "))

# If statement no: 1
if (a % 2 == 0):
    print("Age is even")
# End of If statement no: 1

# If satement no: 2
if (a >= 18):
    print("Allowed to enter")
    print("Good to go!")

elif (a < 0):
    print("You are entering invalid age")

else:
    print("Not allowed to enter")

# End of If statement no: 2

print("End of program")
