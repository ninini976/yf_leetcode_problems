# Construct a 2D array sums[row+1][col+1]

# (notice: we add additional blank row sums[0][col+1]={0} and blank column sums[row+1][0]={0} to remove the edge case checking), so, we can have the following definition

# sums[i+1][j+1] represents the sum of area from matrix[0][0] to matrix[i][j]

# To calculate sums, the ideas as below

# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+

#    sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  

#                         matrix[i-1][j-1]

# So, we use the same idea to find the specific area's sum.

# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
# |               |   |         |    |   |   |           |   |         |    |   |   |          |
# |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
# |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
# |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
# |   |      |    |   |         |    |   |   |           |   |              |   |              |
# |   +------+    |   +---------+    |   +---+           |   |              |   |              |
# |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
