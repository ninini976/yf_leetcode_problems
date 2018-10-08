# use DP
# dp[i] = 0: good
# dp[i] = 1: remain unchanged
# dp[i] = 2: invalid

# Notice: power operator in python "**"


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0]*(max(10,N+1))
        dp[2], dp[5], dp[6], dp[9] = 0,0,0,0
        dp[0], dp[1], dp[8] = 1,1,1
        dp[3],dp[4],dp[7] = 2,2,2
        if N < 10:
            return sum([1 if k == 0 else 0 for k in dp[:N+1]])
        
        for i in range(10,N+1):
            log10 = int(math.log(i,10))
            leadingNum = i/(10**log10)
            remainer = i%(leadingNum*10**log10)
            if dp[leadingNum] == 2 or dp[remainer] == 2:
                dp[i] = 2
                continue
            if dp[leadingNum] == 1 and dp[remainer] == 1:
                dp[i] = 1
                continue
            if dp[leadingNum] == 0 or dp[remainer] == 0:
                dp[i] = 0
                continue
            
        return sum([1 if k == 0 else 0 for k in dp])
