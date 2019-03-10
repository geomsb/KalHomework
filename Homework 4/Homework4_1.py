from Account import Account
account1 = Account(1122, 20000, 4.5)
account1.withdraw(2500)
account1.deposit(3000)

print(account1.get_newId())
print(account1.get_balance())
print(account1.getMonthlyInterestRate())
print(account1.getMonthlyInterest())
