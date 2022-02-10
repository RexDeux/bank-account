class Account:
    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance
        pass

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawl(self, amount):
        self.balance = self.balance - amount

        
class SavingsAccount(Account):
    def __init__(self, title=None, balance=None, interestRate= 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        pass

    def interestAmmount(self, balance, interestRate, interest_ammount):
        return(self.interestRate * self.balance) / 100

demo1 = SavingsAccount("Mark", 2000, 5)