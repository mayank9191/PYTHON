# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

trans = {
    "Namaste": "hello",
    "Subha": "Morning",
    "Nashta": "Breakfast",
    "Ratri": "Night",
    "Gadi": "Car",
    "Sukriya": "Thanks",
    "Prithvi": "Earth"
}

print(trans.get(input("Enter your Word in hindi : "), "Translation not found"))
