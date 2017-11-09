class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        
        s1 = list(s)
        s1.reverse()
        return ''.join(s1)
