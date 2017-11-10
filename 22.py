class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur = ''
        # begining of construction
        # nothing in cur, l = 0, r = 0
        self.helper(res, cur, 0 ,0 ,n)
        return res
        
        
    def helper(self, res, cur, l, r, n):
        if len(cur) == 2*n:
            res.append(cur)
            return
        
        # if the # of left is greater than # of right 
        # we can add a right
        if r < l:
            self.helper(res, cur+")", l, r+1,n)
        # if the # of left is less than max left allowed
        # we can add a left
        if l < n:
            self.helper(res, cur+"(", l+1, r, n)
