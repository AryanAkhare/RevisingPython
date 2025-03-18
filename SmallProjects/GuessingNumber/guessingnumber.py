import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name, player_wins, game_count

        while True:
            playechoice = input(f"\n{name}, guess which number I am thinking of... 1, 2, or 3.\n\n")
            if playechoice not in ["1", "2", "3"]:
                print(f"{name}, please enter 1, 2, or 3.")
                continue  # Ask again if input is invalid

            computerchoice = random.choice("123")

            print(f"\n{name}, you chose {playechoice}.")
            print(f"\nI was thinking of choosing {computerchoice}.")

            player = int(playechoice)
            computer = int(computerchoice)

            if player == computer:
                player_wins += 1
                print(f"Congrats {name}, you win!")
            else:
                print(f"Sorry {name}, better luck next time.")

            game_count += 1
            print(f"\nGame count: {game_count}")
            print(f"\n{name}, your win count: {player_wins}")
            print(f"\nYour winning percentage: {player_wins / game_count:.2f}")

            playagain = input(f"\n{name}, wanna play again? (Y for Yes, Q to Quit): ").lower()
            if playagain == "q":
                print("\nThank you for playing!")
                sys.exit(f"\nBye {name}, see ya later.")

    return play_guess_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalized game experience for guessing numbers.")
    parser.add_argument('-n', '--name', metavar='name', required=True, help='The name of the person playing the game.')
    args = parser.parse_args()
    guess_my_number = guess_number(args.name)
    guess_my_number()
