# Write a program to mine a log file and find out whether it contains ‘python’.

with open("Practice_09/log.txt", "r") as f:
    content = f.read()

    if ("Python" in content):
        print("Log file contain python")

    else:
        print("Log file donot contain python")
