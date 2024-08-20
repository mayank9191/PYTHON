try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

# It will run a piece of code when try was successful.
else:
    print("I am inside else")
