class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            #print('i',i)
            if i == 0:
                res.append([1])
                continue
            res.append([])
            res[i].append(1)
            for j in range(len(res[i-1])-1):
                #print('j',j)
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
        return res
