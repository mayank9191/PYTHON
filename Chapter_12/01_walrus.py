# Using walrus operator
if ((n := len([1, 2, 3, 4, 5])) > 3):
    print(f"List is too long ({n} elements, expected <= 3)")

# ":=" used to assign a value inside an expression like in if statement or while loop
