# use recursion to compare two trees


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and not q:
            return False
        if q and not p:
            return False
        if not p and not q:
            return True
        if p and q:
            if p.val == q.val:
                return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
            else:
                return False
