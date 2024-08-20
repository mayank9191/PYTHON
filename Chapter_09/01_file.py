# open("filename", "mode of opening(read mode by default)")
f = open("Chapter_09/file.txt", "r")

# read its content
data = f.read()

# print its content
print(data)

# close the file
f.close()
