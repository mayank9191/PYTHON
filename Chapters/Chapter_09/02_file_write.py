# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode. WRITE FILES

st = "Hey Mayank you are amazing"

f = open("Chapter_09/myfile.txt", "w")

f.write(st)


f.close()
