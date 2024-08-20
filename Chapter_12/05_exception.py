try:
    a = int(input("Hey, Enter a number: "))  # execute code or try
    print(a)

except ValueError as v:  # error occurs it takes as v and print
    print(v)

except Exception as e:
    print(e)

print("Thank you!")
