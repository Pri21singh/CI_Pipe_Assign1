import time

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        print(f"Deposited: ${amount}, New Balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        self.balance -= amount
        print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        return self.balance

    def get_balance(self):
        print(f"Current Balance: ${self.balance}")
        return self.balance


if __name__ == "__main__":
    print("Banking Application Started")
    account = BankAccount(100)  # Start with $100 balance
    account.deposit(50)
    account.withdraw(30)
    account.get_balance()

    # Add a wait to keep the container running
    print("Waiting for 20 seconds...")
    time.sleep(20)  # Keeps the container running for 60 seconds
    print("Exiting application after wait.")
