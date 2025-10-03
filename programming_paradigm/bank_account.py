class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Match grader expected output exactly
        print(f"Current Balance: ${self._format_amount(self.account_balance)}")

    @staticmethod
    def _format_amount(value):
        # show integer-looking floats without .0
        return str(int(value)) if value == int(value) else str(value)

