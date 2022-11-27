from account import Account

class Savings(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        self.balance = balance
        if balance < 10:
            raise Exception ('A minimum balance deposit of $10 is required.')
    
    def withdraw(self, withdraw_amt):
        transaction_fee = 2
        after_withdraw = self.balance - transaction_fee - withdraw_amt
        if after_withdraw < 10:
            raise Exception (f'You must maintain a minimum balance of $10. Your current balance is ${self.balance}.')
        else:
            self.balance = after_withdraw
            return f"You have incurred a $2 transaction fee. Your balance is now ${self.balance}."

    def add_interest(self, rate):
        interest = self.balance * rate/100
        self.balance = self.balance + interest
        return f"Your balance is now ${self.balance}."

#my_savings = Savings('1234', 5, '1999-03-27 11:30:09 -0800')
my_savings_2 = Savings('4321', 100, '1999-03-27 11:30:09 -0800')
#print(my_savings_2.withdraw(10)) #You have incurred a $2 transaction fee. Your balance is now $88.
#print(my_savings_2.add_interest(0.25)) #-> 100.25
