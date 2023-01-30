class BankAccount:
    def __init__(self,account_name,starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self,ammount):
        self.balance = self.balance + ammount

    def withdraw(self,ammount):
        if self.balance >= ammount:
            self.balance = self.balance - ammount
        else:
            print("You do not have enough money")
    def get_balance(self):
        return str(self.account_name) +" has a balance of $"+ str(self.balance)