friends = ["Apple", "Orange", 5, 325.4, False, "Aakash",
           "Rohan"]
print(friends)

friends.append("doll")  # add "doll" at the end of list(only 1 at a time)

# insert at specific place place here at 2 index
friends.insert(2, "Pineapple")
print(friends)

friends.pop(3)  # it will remove item from list at given index
print(friends)

friends.remove(False)  # it will remove the list iteam directly by mentioning
print(friends)

friends.reverse()  # it reverse the order of list
print(friends)

# List of integer to sort them in order

number = [2, 6, 1, 20, 15, 50, 100, 5]

number.sort()  # arrange numbers into ascending order (increasing order)
print(number)

number.reverse()
print(number)

number.extend([3, 4])  # use to add more than 1 element in list at last
print(number)

digits = number.copy()  # it creates a shallow copy of list
print(digits)

number.clear()  # it clears list and there is no iteam left
print(number)
