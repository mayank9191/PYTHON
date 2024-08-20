a = int(input("Enter your age : "))

# If elif else ladder

if (a >= 18):
    print("Allowed to enter")
    print("Good to go!")

elif (a < 0):
    print("You are entering invalid age")

elif (a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("Not allowed to enter")

print("End of program")
