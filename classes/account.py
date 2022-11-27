import csv

class Account:
    def __init__(self, id, balance, open_date):
        self.id = id
        self.balance = balance
        self.open_date = open_date
        if balance < 0:
            raise Exception ('Please deposit a valid amount.')
    
    def withdraw(self, withdraw_amt):
        after_withdraw = self.balance - withdraw_amt
        if after_withdraw < 0:
            raise Exception (f'Your withdraw request may not exceed your current balance. Your current balance is ${self.balance}.')

    def deposit(self, deposit_amt):
        self.deposit_amt = deposit_amt
        updated_balance = self.balance + deposit_amt
        self.balance = updated_balance
        return f"Your current balance is now ${self.balance}." 

    def check_balance(self):
        return self.balance 
    
    @classmethod
    def all_accounts(cls):
        accounts = []
        with open('../support/accounts.csv', 'r') as account_data_csv:
            accounts_data = csv.DictReader(account_data_csv, delimiter=',')
            for row in accounts_data:
                new_account = row
                accounts.append(new_account)
        return accounts
    
    @classmethod
    def find(cls, id):
        for account in cls.all_accounts():
            if account['id'] == id:
                return account
        return 'Account not found.'

# my_account = Account(1234, 100, '1999-03-27 11:30:09 -0800')
# print(my_account.open_date)
# #print(Account.all_accounts())
# print(Account.find('1212')) #-> {'id': '1212', ' balance': '1235667', ' open_date': '1999-03-27 11:30:09 -0800'}
# print(Account.find('8793')) #-> Account not found.

