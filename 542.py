# doesn't quite understand leetcode discussion answer
# my own use BFS propagate inside from 0 blocks

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dist = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        stack = []
        
        # for line in matrix:
        #     print line
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    if i+1 < len(matrix) and matrix[i+1][j] == 1:
                        dist[i+1][j] = 1
                        stack.append((i+1,j,1))
                    if i-1 > -1 and matrix[i-1][j] == 1:
                        dist[i-1][j] = 1
                        stack.append((i-1,j,1))
                    if j+1 < len(matrix[0]) and matrix[i][j+1] == 1:
                        dist[i][j+1] = 1
                        stack.append((i,j+1,1))
                    if j-1 > -1 and matrix[i][j-1] == 1:
                        dist[i][j-1] = 1
                        stack.append((i,j-1,1))
        
        
        
        while len(stack) > 0:
            i = stack[0][0]
            j = stack[0][1]
            level = stack[0][2]
            stack.pop(0)
            
            if i+1 < len(matrix) and matrix[i+1][j] == 1 and dist[i+1][j] == -1:
                dist[i+1][j] = level + 1
                stack.append((i+1,j,level+1))
            if i-1 > -1 and matrix[i-1][j] == 1 and dist[i-1][j] == -1:
                dist[i-1][j] = level + 1
                stack.append((i-1,j,level+1))
            if j+1 < len(matrix[0]) and matrix[i][j+1] == 1 and dist[i][j+1] == -1:
                dist[i][j+1] = level + 1
                stack.append((i,j+1,level+1))
            if j-1 > -1 and matrix[i][j-1] == 1 and dist[i][j-1] == -1:
                dist[i][j-1] = level + 1
                stack.append((i,j-1,level+1))
        
        # print ''
        # for line in dist:
        #     print line
        
        return dist
