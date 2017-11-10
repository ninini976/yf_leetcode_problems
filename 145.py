# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# construct the answer in a reverse order
# postorder: left, right, val
# reversely: val, right, left
#     within right: right.val, right.right, right.left
# the element before val is the rootval for tree right

# everytime insert at the beginning of the answer list
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if not root:
            return []
        stack.append(root)
        # do a preorder then reverse
        res = []

        while stack:
            node = stack.pop()
            res.insert(0,node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return res    
