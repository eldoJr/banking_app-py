class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self._record_transaction("Interest Applied", interest)
        print(f"Interest applied. Amount: ${interest:.2f}")