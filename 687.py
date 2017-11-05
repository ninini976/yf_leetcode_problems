# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # return two values
    # 0: path, longest uni path given the current node as root
    # 1: pathdown, longest uni path that only goes down given the current node as root
    
    def helper(self, root, level):
        if not root:
            return 0,0
        
        
        
        paths = []
        pathsdown = []

        path, pathdown = self.helper(root.left,level+1)
        paths.append(path)
        pathsdown.append(pathdown)
        
        path, pathdown = self.helper(root.right,level+1)
        paths.append(path)
        pathsdown.append(pathdown)

        concat1 = 0
        concat2 = 0
        if root.left and root.left.val == root.val:
            concat1 += pathsdown[0] + 1
        if root.right and root.right.val == root.val:
            concat2 += pathsdown[1] + 1
        
        maxpath = max(paths)
        maxpath = max(maxpath, concat1+concat2)
        
        # print(level, root.val, maxpath, concat)
        
        return maxpath, max(concat1, concat2)
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans, pathdown = self.helper(root, 0)
        return ans
        
