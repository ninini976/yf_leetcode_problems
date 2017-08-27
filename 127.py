# use double end BFS
# remember to remove visited from wordDict
# change front and back according to need
# use of set operations like '&' , '-'
# other useful operations check https://docs.python.org/2/library/sets.html
# interesting way to do BFS(find neighbour)

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        length = 2
        wordDict = set(wordDict)
        front, back = set([beginWord]), set([endWord])
        if beginWord in wordDict:
            wordDict.remove(beginWord)
        if not endWord in wordDict:
            return 0
        while front:
            #print("front",front)
            #print("back",back)
            front = wordDict & set([word[:i] + char + word[i+1:] for char in 'abcdefghijklmnopqrstuvwxyz' for i in range(len(beginWord)) for word in front])
            if front & back:
                return length
            if len(front) > len(back):
                front, back = back, front
            wordDict -= front
            length += 1
        return 0
