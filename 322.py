#自写递动态规划、递归，超时
def coinChange(coins, amount):
    minCoin = min(coins)
    if amount == 0:
        return 0
    if amount < minCoin:
        return -1
    next = []
    for coin in coins:
        if amount == coin:
            return 1
        result = coinChange(coins, amount - coin)
        if result == -1:
            continue
        next.append(result)
    if len(next) == 0:
        return -1
    else:
        return min(next)+1
coins = [1,2,5]
amount = 11
print (coinChange(coins, amount))