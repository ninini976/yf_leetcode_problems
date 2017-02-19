# only need to record one column is enough
# another idea can be calculate math formula as solution 

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cur = [1 for _ in range(m)]
        for i in range(n-1):
            for j in range(m-1):
                cur[j+1] += cur[j]
        return cur[-1]
