# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

outoff = int(input("Enter max marks for each subject : "))

maths = int(input(f"Enter your Mathematics marks (out of {outoff} ): "))
sci = int(input(f"Enter your Science marks (out of {outoff} ) : "))
his = int(input(f"Enter your History marks (out of {outoff} ) : "))

total = maths + sci + his

if (0 <= maths <= outoff and 0 <= sci <= outoff and 0 <= his <= outoff):
    if (total >= ((3*outoff)*0.4)):
        if (maths >= outoff*0.33 and sci >= outoff*0.33 and his >= outoff*0.33):
            print("Congratulation! You have passed ")

        else:
            print("You didn't make it. Minimum 33% required in each subject.")

    else:
        print("You didn't make it. Total marks should be at least 40% of the total possible marks.")

else:
    print("You are entering that only happen with Apsara dark pencil !")
