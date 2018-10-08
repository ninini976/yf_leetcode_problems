# recursion
# root.left = addOneRow(root.left, v, d-1)
# root.right = addOneRow(root.right, v, d-1)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        
        if d == 2:
            left = root.left
            right = root.right
            newLeft = TreeNode(v)
            newRight = TreeNode(v)
            root.left = newLeft
            root.right = newRight
            newLeft.left = left
            newRight.right = right
            return root
        
        left = self.addOneRow(root.left,v,d-1)
        right = self.addOneRow(root.right,v,d-1)
        root.left = left
        root.right = right
        
        return root
