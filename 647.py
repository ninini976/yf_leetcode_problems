# first get to mid point
# then extend palindrom


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def extendP(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += extendP(s, i, i)
            count += extendP(s, i, i+1)
        return count
        
