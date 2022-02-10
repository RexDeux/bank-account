class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawl(self, amount):
        self.balance = self.balance - amount

        
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate= 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        

    def interestAmount(self):
        return(self.interestRate * self.balance / 100)

demo1 = SavingsAccount("Nuno", 10000, 2.5)
print("Initial Balance:", demo1.getBalance())
demo1.withdrawl(2500)
print("Balance after withdrawal:", demo1.getBalance())
demo1.deposit(500)
print("Balance after deposit:", demo1.getBalance())
print("Interest on current balance:", demo1.interestAmount())