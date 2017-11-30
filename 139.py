# simple dp solution
# dp[i] boolean whether s[:i] can broke into w in words

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                # last len(w) letters same as w
                # and dp[i-len(w)] is true or i-len(w) goes to beginning
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
