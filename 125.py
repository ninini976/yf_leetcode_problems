# useful python functions for this question
# .isalnum()
# .lower()
# use two pointers, one move from front to end, one move from end to beginning
# corner case to consider
# ''
# 'a.'
# '.,'



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            #print(left, right)
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            #print(left, right)
            
            if left <= right:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
        return True
