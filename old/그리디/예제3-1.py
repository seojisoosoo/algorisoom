n = 1260  # 줘야할 거스름돈
coins = {500: 0, 100: 0, 50: 0, 10: 0}
money = n

for coin in coins.keys():
    coins[coin] = money//coin
    money = money % coin
print(coins)
