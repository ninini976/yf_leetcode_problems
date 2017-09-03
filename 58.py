# not hard, many corner cases to handle
# s = ''
# s = ' '
# s = 'a '


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = ''
        if not s:
            return 0
        # s = 'a '
        # s = ' '
        last = len(s) - 1
        while last >= 0 and s[last] == ' ':
            last -= 1
        if last < 0:
            return 0
        i = last
        while i >= 0:
            if s[i] == ' ':
                break
            else:
                i -= 1
        return last-i
