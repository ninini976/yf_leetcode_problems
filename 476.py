# xxxxxx
# 111111
# xor
# result



class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        #print(i-1)
        return (i - 1) ^ num
