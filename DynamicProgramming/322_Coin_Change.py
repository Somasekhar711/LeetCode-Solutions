class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


# Approach: Bottom-up dynamic programming computing minimum coins for each amount up to target.
# Time Complexity: O(amount * len(coins)) as we compute dp for each amount and iterate coins.
# Space Complexity: O(amount) for the dp array.