import sys
import random
from enum import Enum

def rps():
    # Track game statistics
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins, game_count

        # Enum to represent choices
        class RPS(Enum):
            rock = 1
            paper = 2
            scissor = 3

        print("\nEnter your choice:")
        player_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")

        # Validate input
        if player_choice not in ["1", "2", "3"]:
            print("Invalid input! Please enter 1, 2, or 3.")
            return play_rps()  # Recursive call to retry

        player = int(player_choice)
        computer = random.choice([1, 2, 3])  # Random choice for computer

        print(f"\nYou chose {RPS(player).name}.")
        print(f"Computer chose {RPS(computer).name}.\n")

        # Determine the winner
        def decide_winner(player, computer):
            nonlocal player_wins, python_wins
            
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return "You win! 😎"
            elif player == computer:
                return "It's a tie! 🪢"
            else:
                python_wins += 1
                return "Computer wins! 🤖"

        # Display the result
        print(decide_winner(player, computer))
        
        game_count += 1
        
        # Display game statistics
        print(f"\nGames played: {game_count}")
        print(f"Your Wins: {player_wins}, Computer Wins: {python_wins}\n")
        
        # Ask to play again
        while True:
            play_again = input("Play again? (Y for Yes, N for No): ").lower()
            if play_again in ["y", "n"]:
                break
            print("Invalid input! Enter Y or N.")
        
        if play_again == "y":
            return play_rps()  # Restart game
        else:
            print("\n🥳 Thank you for playing!")
            sys.exit("Bye! 👋")  # Exit program

    return play_rps

# Start the game
play = rps()
play()
