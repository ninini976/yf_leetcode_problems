# dp solution, easy


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        if n <= 2:
            return dp[n]
        else:
            i = 3
            while i < n:
                dp.append(dp[i-1]+dp[i-2])
                i += 1
            return dp[i-1]+dp[i-2]
