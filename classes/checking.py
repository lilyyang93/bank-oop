from account import Account

class checking(Account):
    
    check_withdraw_counter = 0
    
    def withdraw(self, withdraw_amt):
        transaction_fee = 1
        after_withdraw = self.balance - transaction_fee - withdraw_amt
        if after_withdraw < 0:
            raise Exception (f'Your requested withdraw amount exceeds your current balance. Your current balance is ${self.balance}.')
        else:
            self.balance = after_withdraw
            return f"You have incurred a $1 transaction fee. Your balance is now ${self.balance}."
    
    def withdraw_using_check(self, amount):
        transaction_fee = 2
        while self.check_withdraw_counter < 3:
            after_check_withdraw = self.balance - amount
            if after_check_withdraw < -10:
                return f"Check withdrawal failed to process due to exceeding maximum overdraft amount. Current balance: ${self.balance}" 
            else:
                self.balance = self.balance - amount
                self.check_withdraw_counter += 1
                return (f"Your balance is now ${self.balance}.")
        after_check_withdraw = self.balance - amount - transaction_fee
        if after_check_withdraw < -10:
            return f"Check withdrawal failed to process due to exceeding maximum overdraft amount. Current balance: ${self.balance}"
        else:
            self.balance = after_check_withdraw
            return (f"Your balance is now ${self.balance}.")
    
    def reset_checks(self):
        self.check_withdraw_counter = 0


my_checking = checking('1234', 100, '1999-03-27 11:30:09 -0800')
my_checking.withdraw_using_check(10)
my_checking.withdraw_using_check(10)
my_checking.withdraw_using_check(10)
print(my_checking.withdraw_using_check(10)) #-> "Your balance is now $58."
my_checking.reset_checks()
print(my_checking.withdraw_using_check(10)) #-> "Your balance is now $48."

#   - The user is allowed three free check uses in one month, but any subsequent use adds a $2 transaction fee
# - `reset_checks()`: Resets the number of checks used to zero
