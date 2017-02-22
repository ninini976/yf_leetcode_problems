# problem solving idea: dynamic programing
# important induction function:
# helper(start,end) = min([ i + max(helper(start, i-1), helper(i+1,end)) for i in range(start+1,end)])


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        result = self.helper(1,n,dict)
        # print dict
        return result
        
    def helper(self, start, end, dict):
        
        if not dict[start][end] == -1:
            return dict[start][end]
        if start == end:
            dict[start][end] = 0
            return 0
        elif start == end - 1:
            dict[start][end] = start
            return start
        elif start == end - 2:
            dict[start][end] = start + 1
            return start + 1
        else:
            result = min([ (i + max([self.helper(start,i-1,dict), self.helper(i+1, end, dict)])) for i in range(start+1,end)])
            dict[start][end] = result
            return result
