# Guess The Number
# Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is.
# # If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.
import random
from datetime import datetime


guessed = False
playing = "yes"
while "y" in playing:
    guessed = False
    random.seed(datetime.now())
    random_number = random.randint(0, 20)
    while guessed != True:
        inp = int(input("Guess the number: "))
        if inp == random_number:
            guessed = True
            print("Congratulations! You guessed!")
            playing = str(input("Would you like to play again? yes/no: "))

        elif inp > random_number:
            print("Hidden number is smaller")

        elif inp < random_number:
            print("Hidden number is bigger")
else:
    print("Ok, bye-bye")
