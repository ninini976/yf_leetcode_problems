# use helper function to do recursion
# pass down level and res
# level by level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.helper(root, 0, res)
        return list(reversed(res))
        
    def helper(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)
