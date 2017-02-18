# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#idea: count the number of elements in left tree, if > k  then the kth smallest element is the kth smallest element in left tree
# if == k-1 then root is the kth smallest element
# if < k-1 then find the k-1-count th smallest element in the right tree

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lcount = self.count(root.left)
        if lcount == k-1:
            return root.val
        if lcount >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-1-lcount)
            
    def count(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.count(root.left) + self.count(root.right)
