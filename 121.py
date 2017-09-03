# This problem is very much similar to maxsubarray
# Use the same dp solution
# dp[i] = max profit you can make by selling stock at time i

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = []
        dp.append(0)
        for i in range(len(prices)-1):
            dp.append(max(0,dp[i] + prices[i+1] - prices[i]))
        return max(dp)
