import sys
import guessingnumber
import RPS7

def main_menu():
    while True:
        print("\n\ud83c\udfae Welcome to the Arcade! \ud83c\udfae")
        print("1. Play Guess the Number")
        print("2. Play Rock, Paper, Scissors")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            name = input("Enter your name: ")
            game = guessingnumber.guess_number(name)
            try:
                game()
            except SystemExit:
                continue  # Return to menu after game exits
        elif choice == "2":
            name = input("Enter your name: ")
            game = RPS7.rps(name)
            try:
                game()
            except SystemExit:
                continue  # Return to menu after game exits
        elif choice == "3":
            print("\nThanks for visiting the arcade! \ud83c\udf89")
            sys.exit("Goodbye! \ud83d\udc4b")
        else:
            print("Invalid input! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()