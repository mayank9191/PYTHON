# Repeat program 4 for a list of such words to be censored.

replace = "#"

find = ["donkey", "the", "animal"]

with open("Practice_09/text.txt", "r") as f:
    content = f.read()

new_content = content

for i in find:
    if (i in content):
        new_content = new_content.replace(i, replace*len(i))

    else:
        print(f"Text.txt donot contain {find}")

with open("Practice_09/text.txt", "w") as r:
    r.write(new_content)
