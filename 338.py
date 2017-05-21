# i&(i-1) will remove the right most bit 1 in the binary number i
# right most bit "1" of i will change to "0" after the operation i&(i-1)

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1,num+1):
            res[i] = res[i&(i-1)]+1
        return res
