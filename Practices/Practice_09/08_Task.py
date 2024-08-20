# Write a program to make a copy of a text file “this. txt”

with open("Practice_09/this. txt", "r") as f:
    content = f.read()

with open("Practice_09/copy_this.txt", "w") as r:
    r.write(content)
    print("text of this.txt is got copy into copy_this.txt")
