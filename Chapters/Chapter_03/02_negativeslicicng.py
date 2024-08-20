name = "mayank"

# Negative Indexing

nameshort = name[-4:-2]  # in negative indexing starts from -1

#  (  M  A  Y   A   N   K )
#  (  0  1  2   3   4   5 )
#  ( -6 -5 -4  -3  -2  -1 )

print(nameshort)
print(name[2:4])


print(name[:3])  # Indexing starts from 0 if nothing written
print(name[1:])  # Indexing end at len(name) if nothing written

# SLICING WITH SKIP VALUE

a = "mayank"
print(a[0:6:3])
