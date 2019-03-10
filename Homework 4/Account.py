class Account:
    def __init__ (self, newId = 0, balance = 100.0, annualInterestRate =0.0):
        self.__newId = newId
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

#Mutator Methods
    def set_newId (self, newId):
        self.__newId = newId

    def set_balance (self, balance):
        self.__balance = balance

    def set_annualInterestRate (self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

#Accesor Methods

    def get_newId (self):
        return self.__newId

    def get_balance (self):
        return self.__balance

    def get_annualInterestRate (self):
        return self.__annualInterestRate

#Method
    def getMonthlyInterestRate (self):
        MontlyInterestRate = (self.__annualInterestRate)/12
        return MontlyInterestRate

    def getMonthlyInterest (self):
        return (self.getMonthlyInterestRate()/100) *self.__balance

    def withdraw (self, amount):
        self.__balance -= amount

    def deposit (self, amount):
        self.__balance += amount

