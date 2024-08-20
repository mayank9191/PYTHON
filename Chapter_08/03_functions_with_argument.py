def greet(name, ending):  # we can give parameter direct to func
    print("Good day, "+name.title() + " sir")
    print(ending)
    return "done"


a = greet("mayank", "Thank you!")

print(a)
