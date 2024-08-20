# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

# very good question

import random


def game():
    print("You are playing the game..")
    score = random.randint(1, 63)
    print(f"Your score: {score}")
    return score


new_score = game()

with open("Practice_09/Hi-score.txt", "r") as f:
    score = f.read()
    if (score != ""):
        score = int(score)
    else:
        score = 0
    print(f"Your old score {score}")
    if (score < new_score):
        with open("Practice_09/Hi-score.txt", "w") as f:
            f.write(str(new_score))
            print(f"Your new score {new_score}")
