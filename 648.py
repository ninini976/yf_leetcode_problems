class Node(object):
    def __init__(self):
        self.children = {}
        self.isend = 0
        
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = Node()
                current = current.children[char]
        current.isend = 1
        
    def shortestprefix(self, word):
        current = self.root
        count = 0
        for char in word:
            # if can find the char
            if char in current.children:
                current = current.children[char]
                count += 1
                # keep going or return prefix
                if current.isend:
                    return word[:count] 
            # cannot find char, prefix doesn't exist
            else:
                return word
        # this handles the case when
        # "rabb" in dict, search shortestprefix for "r"
        return word
                


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # use a Trie structure
        trie = Trie()
        # insert everything into the dict
        for item in dict:
            trie.insert(item)
        res = []
        for word in sentence.split(' '):
            res.append(str(trie.shortestprefix(word)))
    
        return str(' '.join(res))
   
