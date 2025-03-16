# Version 2 of RPS
import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        rock = 1
        paper = 2
        scissor = 3

    print("")
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3")
        return play_rps()  # Call the function instead of returning it

    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win! 😎")
    elif player == computer:
        print("It's a tie! 🪢")
    else:
        print("Computer wins! 🤖\n")

    while True:
        playagain = input("\nPlay again? \nY for Yes or\nN for Quit\n\n").lower()
        if playagain in ["y", "n"]:
            break

    if playagain == "y":
        return play_rps()  # Proper recursive call
    else:
        print("\n🥳 Thank you for playing!\n")
        sys.exit("Bye! 👋")  # Exit only when the user chooses to quit

# Call the function at the end
play_rps()
