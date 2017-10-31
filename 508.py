# use a dict to store sum -> freq pair


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        freq = {}
        
        def calAndSaveSum(Node):
            if not Node:
                return 0
            
            sum = Node.val
            sum += calAndSaveSum(Node.left)
            sum += calAndSaveSum(Node.right)
            if sum in freq:
                freq[sum] += 1
            else:
                freq[sum] = 1
            return sum
        
        calAndSaveSum(root)
        
        max_freq = -1
        for key,val in freq.iteritems():
            if val > max_freq:
                max_freq = val
        res = []
        for key,val in freq.iteritems():
            if val == max_freq:
                res.append(key)
        return res
