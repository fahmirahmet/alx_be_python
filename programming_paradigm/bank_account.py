class BankAccount:
    def __init__(self, account_balance=0.0):
        # store balance as float so formatting is predictable
        self.account_balance = float(account_balance)

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # print with exactly two decimal places as the grader expects
        print(f"Current Balance: ${self.account_balance:.2f}")
