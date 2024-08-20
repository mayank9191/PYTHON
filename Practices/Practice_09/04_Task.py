# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

find = "donkey"
replace = "#"

with open("Practice_09/text.txt", "r") as f:
    content = f.read()

if (find in content):
    new_content = content.replace(find, replace*len(find))
    with open("Practice_09/text.txt", "w") as r:
        r.write(new_content)

else:
    print(f"Text.txt donot contain {find}")
