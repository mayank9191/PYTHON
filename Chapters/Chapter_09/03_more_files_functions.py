f = open("Chapter_09/file.txt", "r")

# lines = f.readlines()  # it creates a list of all lines in given file

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()
