from Stock import Stock

stock1 = Stock("INTC", "Intel", 20.5, 20.35)

print(stock1.getStockCurrentPrice())

stock1.setStockCurrentPrice(40)

print(stock1.getStockCurrentPrice())

print(stock1.getChangePercent())
