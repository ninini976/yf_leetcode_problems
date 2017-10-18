# if the input is "aab", check if [0,0] "a" is palindrome. then check [0,1] "aa", then [0,2] "aab".
# While checking [0,0], the rest of string is "ab", use ab as input to make a recursive call.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(len(s)):
            if self.isPalindrome(s, 0, i):
                if not i == len(s)-1:
                    res += [[s[:i+1]]+l for l in self.partition(s[i+1:])]
                else:
                    res += [[s]]
        return res    
    
    def isPalindrome(self, s, i, j):
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
