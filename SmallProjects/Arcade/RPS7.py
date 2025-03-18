import sys
import random
from enum import Enum

def rps(nameofPlayer='Aryan'):
    # Track game statistics
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal nameofPlayer,player_wins, python_wins, game_count

        # Enum to represent choices
        class RPS(Enum):
            rock = 1
            paper = 2
            scissor = 3

        print(f"\n{nameofPlayer} please enter your choice:")
        player_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")

        # Validate input
        if player_choice not in ["1", "2", "3"]:
            print(f"{nameofPlayer} its a invalid input! Please enter 1, 2, or 3.")
            return play_rps()  # Recursive call to retry

        player = int(player_choice)
        computer = random.choice([1, 2, 3])  # Random choice for computer

        print(f"\n{nameofPlayer} you chose {RPS(player).name}.")
        print(f"Computer chose {RPS(computer).name}.\n")

        # Determine the winner
        def decide_winner(player, computer):
            nonlocal nameofPlayer,player_wins, python_wins
            
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return f"{nameofPlayer} you win! 😎"
            elif player == computer:
                return f"{nameofPlayer} its  a tie! 🪢"
            else:
                python_wins += 1
                return f"Bad luck {nameofPlayer} python wins 🤖."

        # Display the result
        print(decide_winner(player, computer))
        
        game_count += 1
        
        # Display game statistics
        print(f"\n{nameofPlayer} you played {game_count} games.")
        print(f"Your Wins: {player_wins}, Computer Wins: {python_wins}\n")
        
        # Ask to play again
        while True:
            play_again = input(f"{nameofPlayer} wanna play again? (Y for Yes, N for No): ").lower()
            if play_again in ["y", "n"]:
                break
            print("Invalid input! Enter Y or N.")
        
        if play_again == "y":
            return play_rps()  # Restart game
        else:
            print(f"\n🥳 Thank you for playing {nameofPlayer}!")
            sys.exit(F"Bye {nameofPlayer} have a great day! 👋")  # Exit program

    return play_rps

# Start the game

if __name__=="__main__":
    import argparse #command line library and arguments
    parser=argparse.ArgumentParser(
        description="Provides personalized game experience."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of person playing the game."
    )

    
    args=parser.parse_args()
    
    rock_paper_scissors = rps()
    rock_paper_scissors()


#Running this file
#py RPS7.py -n "Aryan"