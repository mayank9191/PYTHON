# Write a program to find out whether a file is identical & matches the content of another file.

with open("Practice_09/this.txt", "r") as f:
    content1 = f.read()

with open("Practice_09/copy_this.txt") as r:
    content2 = r.read()

if (content1 == content2):
    print("Both file is identical and matches the content")

else:
    print("Both file is not identical ")
