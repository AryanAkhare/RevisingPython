# oopproject.py - OOPs Bank Account Project
from bankacc import *

def main():
    print("\n🏦 Welcome to the Bank Account Management System!\n")

    # Creating accounts
    aryan = BankAccount(2000, "Aryan")
    kush = BankAccount(1100, "Kush")
    paras = InterestRewardAcc(900, "Paras")
    blaze = SavingAcc(1000, "Blaze")

    while True:
        print("\n🔹 Choose an action:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            name = input("\nEnter account name: ").strip()
            amount = float(input("Enter deposit amount: "))
            account = locals().get(name.lower())
            if account:
                account.deposit(amount)
            else:
                print("\n❌ Account not found.")

        elif choice == "2":
            name = input("\nEnter account name: ").strip()
            amount = float(input("Enter withdrawal amount: "))
            account = locals().get(name.lower())
            if account:
                account.withdraw(amount)
            else:
                print("\n❌ Account not found.")

        elif choice == "3":
            sender_name = input("\nEnter sender's account name: ").strip()
            receiver_name = input("Enter recipient's account name: ").strip()
            amount = float(input("Enter transfer amount: "))
            sender = locals().get(sender_name.lower())
            receiver = locals().get(receiver_name.lower())

            if sender and receiver:
                sender.transfer(amount, receiver)
            else:
                print("\n❌ One or both accounts not found.")

        elif choice == "4":
            name = input("\nEnter account name: ").strip()
            account = locals().get(name.lower())
            if account:
                account.get_balance()
            else:
                print("\n❌ Account not found.")

        elif choice == "5":
            print("\n👋 Thank you for using our system. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
