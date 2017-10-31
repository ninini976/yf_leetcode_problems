# preorder traversal to create string
# recover tree using string
# careful with null value


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        
        stack = []
        stack.append(root)
        
        string =""
        
        while len(stack) != 0:
            node = stack.pop()
            if not node:
                string += "N "
            else:
                string += str(node.val) + " "
                if node.right or node.left:
                    stack.append(node.right)
                    stack.append(node.left)
        print(string)
        return string[:-1]
                
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # corner case
        if not data:
            return None
        nums = data.split(' ')
        
        def buildtree(nums):
            # []
            if not nums:
                return None
            # root N 
            if nums[0] == "N":
                return None
            # only one element
            if len(nums) == 1:
                return TreeNode(int(nums[0]))
            else:
                node = TreeNode(int(nums[0]))
                # find root for right child
                for i in range(len(nums)):
                    # handle null value in list
                    if nums[i] != "N" and int(nums[i]) > node.val:
                        break
                # build tree recursively
                node.left = buildtree(nums[1:i])
                node.right = buildtree(nums[i:])
                return node
        
        
        return buildtree(nums)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
