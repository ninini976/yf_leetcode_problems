# easy to slove use recursion


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [x for x in range(26)]
        if len(s) == 1:
            return nums[(ord(s) - ord("A"))]+1
        else:
            return self.titleToNumber(s[:-1])*26 + nums[(ord(s[-1]) - ord("A"))]+1
