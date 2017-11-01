# create a dict to count frequency

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        
        oddFlag = 0
        count = 0
        for key,val in dict.iteritems():
            # print(key)
            if val%2 == 1 and oddFlag == 0:
                count += val
                oddFlag = 1
            elif val%2 == 1:
                count += val-1
            else:
                count += val
            # print(count)
        return count
