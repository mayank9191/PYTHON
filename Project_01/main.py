'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([1, -1, 0])

choices = {"s": 1,   "w": -1,  "g": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

choice = input("Enter your choice from(s,w,g): ").lower()

if (choice in choices):
    num = choices[choice]
    print(f"You chose: {reverse[num]}\ncomputer chose: {reverse[computer]}")

    if (computer == num):
        print("Game Tie!")

    elif (computer == -1 and num == 0):
        print("You lose! Water drowns gun.")

    elif (computer == -1 and num == 1):
        print("You win! Snake drinks water.")

    elif (computer == 1 and num == -1):
        print("You lose! Snake drinks water.")

    elif (computer == 1 and num == 0):
        print("You win! Gun shoots snake.")

    elif (computer == 0 and num == 1):
        print("You lose! Gun shoots snake.")

    elif (computer == 0 and num == -1):
        print("You win! Water drowns gun.")

else:
    print("Invalid input! Please choose s, w, or g.")
