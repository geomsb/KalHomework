from tkinter import *

class InvestmentValueCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment Value Calculator")
        
        Label(window, text = "Investment Amount").grid(row = 1, column = 1)
        Label(window, text = "Years").grid(row = 2, column = 1)
        Label(window, text = "Annual Interest Rate").grid(row = 3, column = 1)
        Label(window, text = "Future Value").grid(row = 4, column = 1)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar, justify = RIGHT).grid(row = 1, column = 2)
        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar, justify = RIGHT).grid(row = 2, column = 2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 3, column = 2)
        
        self.futureValueVar = StringVar()
        Label(window, textvariable = self.futureValueVar, justify = RIGHT).grid(row = 4, column = 2, sticky = E)

        Button(window, text = "Calculate", command = self.calculate).grid(row = 5, column = 2, sticky = E)

        window.mainloop()

    def calculate(self):
        futureValue = self.getFutureValue(float(self.investmentAmountVar.get()),
                                          int(self.yearsVar.get()),
                                          float(self.annualInterestRateVar.get())/12)
        self.futureValueVar.set(format(futureValue,"10.2f"))


    def getFutureValue(self, investmentAmount, years, monthlyInterestRate):
        futureValue = investmentAmount * (1 + monthlyInterestRate)** (years * 12)
        return futureValue

InvestmentValueCalculator()


