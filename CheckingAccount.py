class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            self._record_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or exceeds overdraft limit.")