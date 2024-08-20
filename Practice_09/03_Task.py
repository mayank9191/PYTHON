# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
import os


def tables():
    folder_path = "Practice_09/Multiplication_Tables"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        for i in range(2, 21):
            file_path = os.path.join(folder_path, f"tables_of_{i}.txt")
            with open(file_path, "w") as f:
                for j in range(1, 11):
                    f.write(f"{i} X {j} = {i*j}\n")


tables()
print(f"Multiplication tables from 2 to 20 have been written to the folder 'Multiplication_Tables'")
