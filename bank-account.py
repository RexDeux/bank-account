class Account:
    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance
        pass
    def getBalance(self, title, balance):
        super().__init__(title, balance)
        return balance
    def deposit(self, balance,ammount):
        self.ammount = ammount
        ammount += balance
    def withdrawl(self, balance, ammount):
        self.ammount = ammount
        ammount -= balance
class SavingsAccount(Account):
    def __init__(self, title=None, balance=None, interestRate= 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        pass
    def interestAmmount(self, balance, interestRate, interest_ammount):
        super().__init__(interestRate, balance)
        self.interest_ammount = interest_ammount
        interest_ammount = (self.interestRate * self.balance) / 100

demo1 = SavingsAccount("Mark", 2000, 5)