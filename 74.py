# treat this array as a sorted list
# length / height
# conversion: 
# a[i] = m[i/length][i%length]
# m[x][y] = a[x*length + y]

# main difficulty is to write binary search

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        length = len(matrix[0])
        height = len(matrix)
        
        l = 0
        r = length * height - 1
        
        while l < r:
            mid = (l+r)/2
            print(mid)
            # print(matrix[mid/length][mid%length])
            if matrix[mid/length][mid%length] < target:
                l = mid+1
            elif matrix[mid/length][mid%length] > target:
                r = mid-1
            else:
                return True
            # print(l,r)
        return matrix[l/length][l%length] == target
