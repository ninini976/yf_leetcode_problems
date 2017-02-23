# key dp idea:
# min_num = min([ 1+dp[n-i*i] for i*i<=n, i++])


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        return self.helper(n, dp)
        
    def helper(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        min_num = 1 + self.helper(n-1, dp)
        i = 2
        while i*i <= n:
            min_num = min(min_num, dp[n-i*i]+1)
            i += 1
        dp[n] = min_num
        return min_num
