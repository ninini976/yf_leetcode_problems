'''
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
'''

# slow version, overtime limit

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0
        row = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        col = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        # initialize first column of row[]
        for i in range(len(row)):
            if grid[i][0] != "W":
                j = 0
                while j < len(row[0]) and grid[i][j] != "W":
                    if grid[i][j] == 'E':
                        row[i][0] += 1
                    j += 1
        for i in range(len(row)):
            for j in range(1,len(row[0])):
                if grid[i][j-1] != 'W' and grid[i][j] != 'W':
                    row[i][j] = row[i][j-1]
                    continue
                else:
                    k=j
                    while k < len(row[0]) and grid[i][k] != "W":
                        if grid[i][k] == 'E':
                            row[i][j] += 1
                        k +=1
        # initialize first row of col[]
        for i in range(len(col[0])):
            if grid[0][i] != 'W':
                j = 0
                while j < len(col) and grid[j][i] != "W":
                    if grid[j][i] == 'E':
                        col[0][i] += 1
                    j += 1
        for i in range(len(col[0])):
            for j in range(1,len(col)):
                if grid[j-1][i] != 'W' and grid[j][i] != 'W':
                    col[j][i] = col[j-1][i]
                    continue
                else:
                    k=j
                    while k < len(col) and grid[k][i] != "W":
                        if grid[k][i] == 'E':
                            col[j][i] += 1
                        k +=1
        max_kill = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j] == 'W' and not grid[i][j] == 'E':
                    max_kill = max(max_kill, row[i][j] + col[i][j])
        return max_kill
        
# better version from discussion in Java

'''
int maxKilledEnemies(vector<vector<char>>& grid) {
    int m = grid.size(), n = m ? grid[0].size() : 0;
    int result = 0, rowhits, colhits[n];
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            if (!j || grid[i][j-1] == 'W') {
                rowhits = 0;
                for (int k=j; k<n && grid[i][k] != 'W'; k++)
                    rowhits += grid[i][k] == 'E';
            }
            if (!i || grid[i-1][j] == 'W') {
                colhits[j] = 0;
                for (int k=i; k<m && grid[k][j] != 'W'; k++)
                    colhits[j] += grid[k][j] == 'E';
            }
            if (grid[i][j] == '0')
                result = max(result, rowhits + colhits[j]);
        }
    }
    return result;
}

'''
