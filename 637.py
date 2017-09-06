# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []
        res = []
        self.helper(root, 0, info)
        for sum, a in info:
            # remember to use float there, otherwise python will make it int by default
            res.append(float(sum)/a)
        return res
        
    def helper(self, root, level, info):
        if not root:
            return
        if level == len(info):
            info.append([0,0])
        info[level][0] += root.val
        info[level][1] += 1
        self.helper(root.left, level+1, info)
        self.helper(root.right, level+1, info)
