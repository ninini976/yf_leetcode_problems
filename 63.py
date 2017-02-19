# still only need one column recorded

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # initiate the cur for first column
        cur = [0 for i in range(len(obstacleGrid))]
        # initiate cur[0] for column one
        cur[0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(len(obstacleGrid)-1):
            cur[i+1] = cur[i] if obstacleGrid[i+1][0] == 0 else 0
        
        # do the rest
        for i in range(len(obstacleGrid[0])-1):
            if obstacleGrid[0][i+1] == 1:
                cur[0] = 0
            for j in range(len(obstacleGrid)-1):
                if obstacleGrid[j+1][i+1] == 0:
                    cur[j+1] += cur[j]
                else: # set the plase with obstacle to 0 unique paths
                    cur[j+1] = 0
        return cur[-1]
