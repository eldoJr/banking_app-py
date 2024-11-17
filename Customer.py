class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added for customer {self.name}.")
    
    def show_accounts(self):
        for account in self.accounts:
            account.display_info()
            print("---")

if __name__ == "__main__":
    # Creating customers and accounts
    customer1 = Customer("C001", "Alice")
    savings = SavingsAccount("A12345", "Alice", 1000.0)
    checking = CheckingAccount("A67890", "Alice", 500.0)
    
    customer1.add_account(savings)
    customer1.add_account(checking)

    # Performing transactions
    savings.deposit(200)
    savings.withdraw(150)
    checking.withdraw(600)  # Overdraft example
    savings.transfer(checking, 100)

    # Applying interest
    savings.apply_interest()

    # Display all accounts and their details
    customer1.show_accounts()
