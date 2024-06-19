# 1.13. Simple banking application using inheritance

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} deposited. Current balance: Rs. {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn. Current balance: Rs. {self.balance}")
        else:
            print("Insufficient balance.")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.deposit(interest_amount)
        print(f"Interest applied. Current balance: Rs. {self.balance}")

# Example usage of banking application
savings_account = SavingsAccount('SA123', 5000, 5)
savings_account.deposit(2000)
savings_account.withdraw(1000)
savings_account.apply_interest()
