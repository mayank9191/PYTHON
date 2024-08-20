# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("Practice_09/poems.txt") as f:
    find = "twinkle"
    if (find in f.read().lower()):
        print(f"Yes, poems.txt contains {find}")
    else:
        print(f"No, poems.txt not contains {find}")
