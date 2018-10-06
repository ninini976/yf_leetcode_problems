class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # max left parenthesis number
        high = 0
        # min left parenthesis number
        low = 0
        for c in s:
            if c == "(":
                high += 1
                low += 1
            if c == ")":
                high -= 1
                if low > 0:
                    low -=1
                if high < 0:
                    return False
            if c == "*":
                high += 1
                if low > 0:
                    low -= 1
        return low == 0
