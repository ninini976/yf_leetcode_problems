# use queue to do level order traversal or BFS (ensure up to down), store both node and col into the queue
# use minmax = [,] to record min col and max col (avoid sort)
# print out


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        map = {}
        minmax = [0,0]
        stack = []
        stack.append((root,0))
        while stack:
            
            #print(map)
            node, level = stack.pop()
            if node.left:
                stack.insert(0,(node.left, level-1))
            if node.right:
                stack.insert(0,(node.right, level+1))
            #print(stack)
            if level in map:
                map[level].append(node.val)
            else:
                map[level] = [node.val]
            if level < minmax[0]:
                minmax[0] = level
            if level > minmax[1]:
                minmax[1] = level
        for i in range(minmax[0], minmax[1]+1):
            res.append(map[i])
        return res
