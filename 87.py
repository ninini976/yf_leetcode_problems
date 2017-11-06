# interestingly super easy recursive solution

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        alphabet = [0 for _ in range(26)]
        # build the letter count dict
        for char in s1:
            alphabet[ord(char) - ord('a')] += 1
        for char in s2:
            alphabet[ord(char) - ord('a')] -= 1
        # only continue if two string have the same number for each letters
        if alphabet != [0 for _ in range(26)]:
            return False
        
        # recursive
        for i in range(1,len(s1)):
            # "a|bc" and "a|bc" 
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # "b|ca" and "ca|b"
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
