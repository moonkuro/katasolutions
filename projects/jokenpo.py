# This is a beginner project for me, trying to be as clean and functional as possible.
# It should work like an jokenpo, where you type an input and the machine should randomly give you a input back.
# I designed it to be a BO3-style of rounds!
# -------------------------------------------------
# The next one i'm planning to use Tkinter so i can have a glimpse of how GUIs and HUDs work.

# Imports
import time 
import os
import random
import curses

# Print the starting screen for the user
print("-----------------")
print("     WELCOME!    ")
print("    LET'S PLAY   ")
print("    JO-KEN-PO!   ")
print("-----------------") 

# Wait 5 seconds and clear the console before printing input choice scene
time.sleep(0)
os.system('cls')

# Print the input selection
print("-----------------------------")
print("       PICK YOUR POISON!     ")
print("-----------------------------")
print(" (stone) (scissors) (paper)  ")
print("-----------------------------") 

# Stores the user input and store it as a lowercase value
user_input = input("> ") 
user_input = user_input.lower()

# Machine-generated random number for match
machine_input = random.randrange(1, 4)

# Translates human inputs into numbers for comparation
if user_input == "stone":
    user_input = 1

elif user_input == "scissors":
    user_input = 2

elif user_input == "paper":
    user_input = 3

# Comparation between player input and machine random number
    # If user input Stone:
if user_input == 1 and machine_input == 1:
    print("This is a draw!")

elif user_input == 1 and machine_input == 2:
    print("You won! Stone x Scissors")

elif user_input == 1 and machine_input == 3:
    print("You lost! Stone x Paper")

    # If user input Scissors:
elif user_input == 2 and machine_input == 1:
    print("You lost! Scissors x Stone")

elif user_input == 2 and machine_input == 2:
    print("This is a draw!")

elif user_input == 2 and machine_input == 3:
    print("You won! Scissors x Paper")

    # If user input Paper:
elif user_input == 3 and machine_input == 1:
    print("You won! Paper x Stone")

elif user_input == 3 and machine_input == 2:
    print("You lost! Paper X Scissors")

elif user_input == 3 and machine_input == 3:
    print("This is a draw!")