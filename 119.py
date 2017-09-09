# interativly update the row array from end to beginning

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        res = [0]*rowIndex
        res[0] = 1
        for i in range(rowIndex - 1):
            res[i+1] = 1
            for j in range(rowIndex - 2):
                res[i - j] += res[i - j - 1]
        return res
