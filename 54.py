class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        length = len(matrix[0])
        height = len(matrix)
        
        # start point of each rectangle we print out
        maxstart = math.ceil(min(length, height)/2.0)
        
        for i in range(int(maxstart)):
            
            
            # when the rectangle we go have both height and width > 1
            if length-1-2*i > 0 and height-1-2*i > 0:
                for j in range(length-1-2*i):
                    res.append(matrix[i][j+i])
            
                for j in range(height-1-2*i):
                    res.append(matrix[j+i][-1-i])
                
                for j in reversed(range(length-1-2*i)):
                    res.append(matrix[height-1-i][j+i+1])

                for j in reversed(range(height-1-2*i)):
                    res.append(matrix[j+i+1][i])
            
            # when the rectangle we go have both height and width == 1
            if length-1-2*i == 0 and height-1-2*i == 0:
                res.append(matrix[i][i])
                continue
             
            # when the rectangle we go have one of height or width == 1
            if height-1-2*i == 0:
                for j in range(length-1-2*i+1):
                    res.append(matrix[i][j+i])
                continue
            if length-1-2*i == 0: 
                for j in range(height-1-2*i+1):
                    res.append(matrix[j+i][-1-i])
                continue
        
        return res
