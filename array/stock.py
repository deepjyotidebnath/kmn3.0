prices = [7, 1, 5, 3, 6, 4]
max_profit=0
min_price = prices[0]

for price in prices:
    profit=price-min_price
    min_price=min(min_price, price)
    max_profit=max(profit, max_profit)
print(max_profit)