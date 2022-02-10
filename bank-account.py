class Account:
    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance
        pass

class SavingsAccount(Account):
   def __init__(self, title=None, balance=None, interestRate= 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        pass

#A = SavingsAccount()
#A("Nuno", 10000, 5)