# O(n) solution


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        isInWordFlag = 0
        for i in range(len(s)):
            if not isInWordFlag and s[i] != ' ':
                count += 1
                isInWordFlag = 1
            
            if s[i] == ' ':
                 isInWordFlag = 0
                
        return count
