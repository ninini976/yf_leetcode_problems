# use recursion to traverse the binary tree
# diameter of a binary tree is max(diameter of the left tree, diameter of the right tree, left depth + right depth)
# since we traverse every node, and we update self.best in every traverse, the recursion can be modified as
# max(self.best, depL + depR)

# cauious: single node tree (for example only one node 5) have depth 1, depth = depL + depR + 1
# if not root: return 0 (None node have depth 0)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0
        
        def depth(root):
            if not root:
                return 0
            depL = depth(root.left)
            depR = depth(root.right)
            
            self.best = max(self.best, depL + depR)
            return max(depL,depR) + 1
        
        depth(root)
        return self.best
