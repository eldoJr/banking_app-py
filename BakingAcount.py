import datetime

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record_transaction("Deposit", amount)
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self._record_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def transfer(self, target_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            self._record_transaction(f"Transfer to {target_account.account_number}", amount)
            print(f"Transfer successful. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid transfer amount.")
    
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance:.2f}")
    
    def _record_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": timestamp
        }
        self.transactions.append(transaction)
        self._save_transaction_to_file(transaction)

    def _save_transaction_to_file(self, transaction):
        with open(f"{self.account_number}_transactions.txt", "a") as file:
            file.write(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']:.2f}\n")