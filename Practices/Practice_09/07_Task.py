# Write a program to find out the line number where python is present from ques 6.

with open("Practice_09/log.txt", "r") as f:
    content = f.readlines()

    for i in content:
        if ("Python" in i):
            n = content.index(i)
            print(f"Python is in line {n+1}")
            found = true
            break

if not found:
    print("Python is not present in any line")
