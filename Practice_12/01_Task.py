# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with (
        open("Practice_12/1.txt") as f1,
        open("Practice_12/2.txt") as f2,
        open("Practice_12/3.txt") as f3
    ):

        print("Thank You!")

except FileNotFoundError as e:
    if (e.filename == "Practice_12/1.txt"):
        print("File 1.txt is not present")

    elif (e.filename == "Practice_12/2.txt"):
        print("File 2.txt is not present")

    elif (e.filename == "Practice_12/3.txt"):
        print("File 3.txt is not present")

    else:
        print(f"Some other file error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
