class Account:
    def __init__(self, accountNumber, accountHolder, accountBalance):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.accountBalance = accountBalance
    
    def getBalance(self):
        return self.accountBalance
    
    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
    
    def withdraw(self, amount):
        if amount > self.accountBalance:
            print('you are poor') 
        else :
            self.accountBalance =  self.accountBalance - amount
            print('You withdraw ' + str(amount))





my = Account(123, 'mai', 444)
my.deposit(100)
my.withdraw(500)
print('you balance is ' + str(my.getBalance()))



