n = int(input())
price = list(map(int, input().split()))

max_profit = 0
min_price = float("inf")

for i in price:
    if i < min_price:
        min_price = i
    elif i - min_price > max_profit:
        max_profit = i - min_price

print(max_profit)