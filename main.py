# +++++ PROJECT 1: ROCK, PAPER, SCISSOR GAME   +++++

# We all have played rock, paper, scissor game in our childhood.
# If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

import random

youDict = {
    "r": -1,
    "p": 0,
    "s": 1
}

reverseDict = {
    -1: "Rock",
    0: "Paper",
    1: "Scissor"
}

computer = random.choice([-1, 0, 1])
print("\n**********   ROCK, PAPER & SCISSOR   **********\n")
print("'R' = Rock   |   'P' = Paper    |    'S' = Scissor\n")
youStr = input("Enter your choice: ")

if(youStr not in youDict):
    print("\nWrong Selection! Please selection from 'r', 'p' or 's'")
else:
    you = youDict[youStr]
    print(f"\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

    if(you == computer):
        print("\nIts a Tie!")
    else:
        if(computer == -1 and you == 0):
            print("\nYou Win!")
        elif(computer == -1 and you == 1):
            print("\nYou Lose!")
        elif(computer == 0 and you == -1):
            print("\nYou Lose!")
        elif(computer == 0 and you == 1):
            print("\nYou Win!")
        elif(computer == 1 and you == -1):
            print("\nYou Win!")
        elif(computer == 1 and you == 0):
            print("\nYou Lose!")
        else:
            print("\nERROR! Something went wrong.")