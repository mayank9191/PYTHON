marks = {
    "Rohan": 87,
    "Mayank": 100,
    "Ruhi": 80,
    "Shyam": 45,
    8: "apple"
}

print(marks)  # print dictionary


print(marks.items())  # Returns a list of (key,value)tuples.

print(marks.keys())  # Returns a list containing dictionary's keys.

print(marks.values())  # Returns a list containing dictionary's values.

# Updates the dictionary with supplied key-value pairs.
marks.update({"Shyam": 87})
print(marks)

# use to get value of specific key
# print none if key not found or message written
print(marks.get("Mayank1", "Nhi hai isma"))
print(marks["Mayank1"])     # print error as there is no such key in dictionary
