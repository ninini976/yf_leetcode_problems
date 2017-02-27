# this solution working but took too long time

'''
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # first number in tuple is next starting index for new line, second number is rows added
        if max([len(word) for word in sentence]) > cols:
            return 0
        dp = [(-1,-1) for i in range(cols)]
        
        
        s_idx = 0
        col_idx = 0
        row_idx = 0
        res = 0
        while row_idx < rows:
            #print(dp)
            if s_idx == 0 and not dp[col_idx][0] == -1:
                if row_idx + dp[col_idx][1] < rows:
                    row_idx += dp[col_idx][1]
                    col_idx = dp[col_idx][0]
                    res += 1
                elif row_idx + dp[col_idx][1] == rows and dp[col_idx][0] == 0:
                    return res + 1
                else:
                    return res
            else:
                self.findnext(sentence, col_idx, cols, dp)
        return res
        
        
        
        
    def findnext(self, sentence, start_idx, cols, dp):
        s_idx = 0
        col_idx = start_idx
        row_idx = 0
        while s_idx != len(sentence):    
            # more than one space remaining
            if cols - col_idx - 1 > len(sentence[s_idx]):
                col_idx += len(sentence[s_idx]) + 1
                s_idx += 1
            # exactly fit OR only one space left
            elif cols - col_idx  == len(sentence[s_idx]) or cols - col_idx  -1 == len(sentence[s_idx]):
                col_idx = 0
                row_idx += 1
                s_idx += 1
            # cannot fit 
            else:
                row_idx += 1
                col_idx = 0
                col_idx += len(sentence[s_idx]) + 1
                s_idx += 1
            # print(s_idx, col_idx, row_idx)
        dp[start_idx] = (col_idx, row_idx)
        return 
    '''
    
    
    
# better solution
# key idea: just put the string in to column
# look at the last character in the column
# three cases handle
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        print(s)
        start = 0
        for i in range(rows):
            start += cols
            if s[(start-1) % len(s)] == ' ':
                continue
            elif s[(start-1) % len(s) + 1] == ' ':
                start += 1
            else:
                while start >= 0 and s[(start-1) % len(s)] != ' ':
                    start -= 1
        return start / len(s)
 
 
 
