# PROJECT 2 – THE PERFECT GUESS

import random

random_num = random.randint(1, 101)

print("You are entering in a game THE PERFECT GUESS\nThis Game will give you hint. Try your best!")

n = 1

while (True):
    your_num = int(input("Guess a Number between (1 to 100): "))
    if (random_num > your_num):
        print("Higher Number Please!")

    elif (random_num < your_num):
        print("Lower Number PLease!")

    else:
        print("Congratulations!, You guessed it right.")
        print(f"You took {n} guesses to reach the Number.")
        break

    n += 1
