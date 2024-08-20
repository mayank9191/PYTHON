# PROJECT 1: SNAKE, WATER, GUN GAME

# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

import random

lists = ["snake", "water", "gun"]
dict = {"s": "Snake", "w": "Water", "g": "Gun"}

random_item = random.choice(lists)


player_choice = input(
    "Select your choice (s for snake, w for water, g for gun): ").lower()

if (player_choice in dict):
    print(f"You chose: {dict[player_choice]}\nComputer chose: {random_item}")

    if (random_item[0] == player_choice):
        print("Game Tie!")

    elif (random_item[0] == "s" and player_choice == "w"):
        print("You lose! Snake drinks water.")

    elif (random_item[0] == "s" and player_choice == "g"):
        print("You win! Gun shoots snake.")

    elif (random_item[0] == "w" and player_choice == "g"):
        print("You lose! Water drowns gun.")

    elif (random_item[0] == "w" and player_choice == "s"):
        print("You win! Snake drinks water.")

    elif (random_item[0] == "g" and player_choice == "w"):
        print("You win! Water drowns gun.")

    elif (random_item[0] == "g" and player_choice == "s"):
        print("You lose! Gun shoots snake.")
else:
    print("Invalid input! Please choose s, w, or g.")
