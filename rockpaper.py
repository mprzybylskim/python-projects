# Rock, Paper, Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer. The computer’s answer will be randomly generated,
# while the program will ask the user for their input. This project will better your understanding of while loops and if statements.

import random
from datetime import datetime
score = 0

while -3 < score < 3:
    random.seed(datetime.now())
    random_computer_choice = random.randint(0, 2)
    inp = input("Pick your choice - rock-paper-scissors: ")

    if "r" in inp[0:1]:
        inp = 0
    elif "p" in inp[0:1]:
        inp = 1
    elif "s" in inp[0:1]:
        inp = 2

    print("Rock!") if random_computer_choice == 0 else (
        print("Paper!") if random_computer_choice == 1 else print("Scissors!"))

    if inp == 0:
        if random_computer_choice == 0:
            print("draw!")
        elif random_computer_choice == 1:
            print("ai wins!")
            score -= 1
        elif random_computer_choice == 2:
            print("you win!")
            score += 1

    elif inp == 1:
        if random_computer_choice == 0:
            print("you win!")
            score += 1
        elif random_computer_choice == 1:
            print("draw!")
        elif random_computer_choice == 2:
            print("you lose!")
            score -= 1

    elif inp == 2:
        if random_computer_choice == 0:
            print("you lose!")
            score -= 1
        elif random_computer_choice == 1:
            print("you win!")
            score += 1
        elif random_computer_choice == 2:
            print("draw!")
print(f"you have {score} points! WINNER!") if score > 0 else print(
    f"you have {score} points :( you LOSE!")
