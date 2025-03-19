# bankacc.py - OOPs project with Python (Bank Account Management)

# Custom Exception for Insufficient Balance
class BalanceException(Exception):
    pass

# Base Class: BankAccount
class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"\n✅ Account '{self.name}' created successfully.")
        self.get_balance()

    def get_balance(self):
        print(f"\n💰 Account '{self.name}' has a balance of ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\n💵 Deposited ${amount:.2f} into '{self.name}'.")
        self.get_balance()

    def _is_transaction_viable(self, amount):
        if self.balance >= amount:
            return True
        raise BalanceException(f"\n❌ Insufficient funds! '{self.name}' has only ${self.balance:.2f}.")

    def withdraw(self, amount):
        try:
            self._is_transaction_viable(amount)
            self.balance -= amount
            print(f"\n🏧 Withdrawn ${amount:.2f} from '{self.name}'.")
            self.get_balance()
        except BalanceException as e:
            print(e)

    def transfer(self, amount, recipient):
        try:
            print(f"\n🔄 Initiating transfer of ${amount:.2f} from '{self.name}' to '{recipient.name}'...")
            self._is_transaction_viable(amount)
            self.withdraw(amount)
            recipient.deposit(amount)
            print("\n✅ Transfer successful!")
        except BalanceException as e:
            print(f"\n❌ Transfer failed: {e}")

# Derived Class: InterestRewardAcc (5% extra deposit bonus)
class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        bonus = amount * 0.05
        self.balance += (amount + bonus)
        print(f"\n🎉 Deposited ${amount:.2f} with a 5% bonus (${bonus:.2f}).")
        self.get_balance()

# Derived Class: SavingAcc (withdrawals incur a $5 fee)
class SavingAcc(InterestRewardAcc):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            total_amount = amount + self.fee
            self._is_transaction_viable(total_amount)
            self.balance -= total_amount
            print(f"\n🏧 Withdrawn ${amount:.2f} (including ${self.fee} fee) from '{self.name}'.")
            self.get_balance()
        except BalanceException as e:
            print(e)
