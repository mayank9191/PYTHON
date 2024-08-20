
f = open("Chapter_09/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:

with open("Chapter_09/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file
