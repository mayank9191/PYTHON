# here ending is default argument if we don't pass any value of ending it takes defaut argument

def greet(name, ending="Thank you!"):
    print(f"Good day, {name.title()}")
    print(ending)


greet("mayank", "bye!")
