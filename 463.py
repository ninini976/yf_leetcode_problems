class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i,j)
                if i == 0 and grid[i][j] == 1:
                    p += 1
                if i == len(grid) - 1:
                    if grid[i][j] == 1:
                        p += 1
                else:
                    if not grid[i][j] == grid[i+1][j]:
                        p += 1
                
                if j == 0 and grid[i][j] == 1:
                    p += 1
                if j == len(grid[0]) - 1:
                    if grid[i][j] == 1:
                        p += 1
                else:
                    if not grid[i][j] == grid[i][j+1]:
                        p += 1
        return p
                
