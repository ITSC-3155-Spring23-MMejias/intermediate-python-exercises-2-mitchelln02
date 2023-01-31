from BankAccount import BankAccount
if __name__ =="__main__":

 
        account = BankAccount("Mitchell",700)
        account.deposit(500)
        account.withdraw(200)
        print(account.get_balance())