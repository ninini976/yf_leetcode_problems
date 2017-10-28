# for i in range(9)
# for j in range(9)
# play with i,j such that we check each row/ col/ block in the inner loop


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = set()
            col = set()
            block = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    else:
                        col.add(board[j][i])
                        
                baserow = i/3*3
                basecol = i%3*3
                #print(baserow + j/3,basecol + j%3)
                point = board[baserow + j/3][basecol + j%3]
                if point != '.':
                    if point in block:
                        return False
                    else:
                        block.add(point)
                        
                    
        return True
