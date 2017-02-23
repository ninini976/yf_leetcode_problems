# key idea: start form top right corner

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
                continue
            if matrix[row][col] > target:
                col -= 1
                continue
            if matrix[row][col] == target:
                return True
        return False
