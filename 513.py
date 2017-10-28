# level order traversal using queue
# simple easy



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append(root)
        
        while len(q):
            size = len(q)
            for i in range(size):
                if i == 0:
                    res = q[-1].val
                if q[-1].left:
                    q.insert(0, q[-1].left)
                if q[-1].right:
                    q.insert(0, q[-1].right)
                    
                q = q[:-1]
        return res
