# Write a python program to rename a file to “renamed_by_ python.txt.

with open("Practice_09/rename.txt", "r") as f:
    content = f.read()

with open("Practice_09/renamed_by_ python.txt", "w") as r:
    r.write(content)

print("rename.txt is renamed as renamed_by_ python.txt")
