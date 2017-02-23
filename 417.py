# depth first search

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(matrix):
            return []
        # initiate borders of matrix
        pac = []
        atl = []
        res = []
        for i in range(len(matrix)):
            pac.append((i,0))
            atl.append((i,len(matrix[0])-1))
        for i in range(len(matrix[0])):
            pac.append((0,i))
            atl.append((len(matrix)-1,i))
        grid_pac = self.search(pac, matrix)
        grid_atl = self.search(atl, matrix)
        print()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if grid_pac[i][j] and grid_atl[i][j]:
                    res.append([i,j])
        return res
        
    def search(self, pos, matrix):
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        while len(pos):
            node = pos.pop()
            if visited[node[0]][node[1]] == 0:
                visited[node[0]][node[1]] = 1
            # check S
            if not node[0] == len(matrix) - 1 and visited[node[0]+1][node[1]] == 0 and matrix[node[0]+1][node[1]] >= matrix[node[0]][node[1]]:
                pos.append((node[0]+1,node[1]))
            # check N
            if not node[0] == 0 and visited[node[0]-1][node[1]] == 0 and matrix[node[0]-1][node[1]] >= matrix[node[0]][node[1]]:
                pos.append((node[0]-1,node[1]))
            # check E
            if not node[1] == len(matrix[0])-1 and visited[node[0]][node[1]+1] == 0 and matrix[node[0]][node[1]+1] >= matrix[node[0]][node[1]]:
                pos.append((node[0],node[1]+1))
            # check W
            if not node[1] == 0 and visited[node[0]][node[1]-1] == 0 and matrix[node[0]][node[1]-1] >= matrix[node[0]][node[1]]:
                pos.append((node[0],node[1]-1))
        return visited
