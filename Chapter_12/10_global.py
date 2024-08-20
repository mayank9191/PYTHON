a = 89  # global varriable


def fun():
    global a    # it changes global varriable value inside a function
    a = 3       # local varriable for fun function
    print(a)


fun()
print(a)
