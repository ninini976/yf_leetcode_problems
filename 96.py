# algorithm: DP
# the formula
# res[n] = sum([ res[i] * res[n-i-1] for i in range(n)])
# select a number as root first and then the unique number of trees is product of number of unique left and right trees 

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*(n+1)
        res[0] = 1
        def helper(n):
            if res[n] != 0:
                return res[n]
            else:
                sum = 0
                for i in range(n):
                    sum += helper(i) * helper(n-i-1)
                res[n] = sum
                return sum
        helper(n)
        return res[n]
