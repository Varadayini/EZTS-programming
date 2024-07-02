def minCoins(bill):
    coins = [1, 5, 7]
    dp = [float('inf')] * (bill + 1)
    dp[0] = 0

    for i in range(1, bill + 1):
        for coin in coins:
            if i >=coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[bill] <= bill:

        return dp[bill] 
    else :
        return -1
bill = 18
print("Minimum number of coins needed:",minCoins(bill))
