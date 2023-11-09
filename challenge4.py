#Challenge 4: Implement a Banking Account
#task1

class Account:

    def __init__(self, title=None, balance=0):
        
        self.title = title
        self.balance = balance
#task2

class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
        
        super().__init__(title, balance)
        
        self.interestRate = interestRate

#task3

account_instance = Account("Ashish", 5000)
print(account_instance.title)    
print(account_instance.balance)  

savings_account_instance = SavingsAccount("Ashish", 5000, 5)
print(savings_account_instance.title)        
print(savings_account_instance.balance)      
print(savings_account_instance.interestRate)  
