# rock, paper, scissor game with some simplified logic

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
        if((computer - you) == -1 or (computer - you) == 2):
            print("\nYou Win!")
        else:
            print("\nYou Lose!")

# Below is the logic of if-else condition (subtracted value of computer by value of you)
# computer - you

'''
win = -1 - 0    -1
win = 0 - 1     -1
win = 1 - - 1   2

lose = -1 - 1   -2
lose = 0 - -1   1
lose = 1 - 0    1
'''