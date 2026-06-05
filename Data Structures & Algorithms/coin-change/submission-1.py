class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[0 for j in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0
        
        for j in range(amount+1):
            dp[0][j] = float('inf')
            if j%coins[0] == 0:
                dp[1][j] = j//coins[0]
            else:
                dp[1][j] = float('inf')
        
        for i in range(2, len(coins)+1):
            for j in range(0, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min((1+dp[i][j-coins[i-1]]), dp[i-1][j]);
                else:
                    dp[i][j] = dp[i-1][j]
        ans = dp[len(coins)][amount]
        return -1 if ans == float('inf') else ans

        def coinChangeRcursive(coins: List[int], amount: int, n: int) -> int:
            if amount == 0:
                return 0
            
            if n == 0:
                return float('inf')
            
            if coins[n-1] <= amount:
                return min(1 + coinChangeRcursive(coins, amount-coins[n-1], n), \
                            coinChangeRcursive(coins, amount, n-1))
            else:
                return coinChangeRcursive(coins, amount, n-1)

        #ans = coinChangeRcursive(coins, amount, len(coins))
        #return -1 if ans == float('inf') else ans