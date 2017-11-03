# dp[i][j]: the longest palindromic subsequence's length of substring(i, j)
# State transition:
# dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
# otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
# Initialization: dp[i][i] = 1


class Solution(object):
    def longestPalindromeSubseq(self, s):
        # the trick here can increase speed
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]
