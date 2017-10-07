# simple recursion solve the problem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        lpathlist = self.binaryTreePaths(root.left)
        rpathlist = self.binaryTreePaths(root.right)
        res = []
        for path in lpathlist:
            res.append(str(root.val) + "->"+ path)
        for path in rpathlist:
            res.append(str(root.val) + "->"+ path)
        if not res:
            return [str(root.val)]
        return res
