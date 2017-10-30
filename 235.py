# goto left node if both smaller than root.val
# goto right node if both larger than root.val
# return if not belong to above senarios

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if q.val > root.val and p.val > root.val:
                root = root.right
                continue
            if q.val < root.val and p.val < root.val:
                root = root.left
                continue
            return root
