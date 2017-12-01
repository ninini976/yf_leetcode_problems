# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# basic idea, denote each tree as a string( use pre-order )
# one thing to pay attention: also represent null as string

class Solution(object):
    def findDuplicateSubtrees(self, root):
        def trv(root):
            # put "null" in string 
            if not root: return "null"
            # construct string
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            # append the node under key of string representation of the tree 
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
        
