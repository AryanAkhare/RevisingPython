#Version 2 of RPS
import sys
import random
from enum import Enum

class RPS(Enum):
    rock=1
    paper=2
    scissor=3

# print(RPS(2))
# print(RPS.rock)
# print(RPS['rock'])
# print(RPS.rock.value)
# sys.exit()

playagain=True
while playagain:
    print("")
    playerchoice=input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
    player=int(playerchoice)

    if player<1 | player>3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice=random.choice("123")
    computer=int(computerchoice)

    print("")
    print("You chose "+str(RPS(player)).replace('RPS.','')+".")
    print("Computer chose "+str(RPS(computer)).replace('RPS.','')+".")
    print("")

    if player == 1 and computer ==3:
        print("You win! 😎")
    elif player ==2 and computer ==1:
        print("You win! 😎")
    elif player ==3 and computer ==2:
        print("You win! 😎")
    elif player ==computer:
        print("Its a tie! 🪢")
    else:
        print("Computer wins! 🤖\n")
    
    playagain=input("\nPlay again? \nY for Yes or\nN for Quit\n\n")
    if playagain.lower()=="y":
        continue
    else:
        print("\n🥳")
        print("Thank you for playing\n")
        playagain=False

sys.exit("Bye! 👋")