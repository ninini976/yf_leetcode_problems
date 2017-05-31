#DP
class Solution(object):
  def generateTrees(self, n):
      """
      :type n: int
      :rtype: List[TreeNode]
      """
      # handle the corner case
      if not n:
          return []
      return self.genTree(1,n)


  def genTree(self, a, b):
      print(a,b)
      if a > b:
          return [None]

      res = []

      for root_num in range(a,b+1):
          left = self.genTree(a,root_num-1)
          right = self.genTree(root_num+1,b)

          for lroot in left:
              for rroot in right:
                  root = TreeNode(root_num)
                  root.left = lroot
                  root.right = rroot
                  res.append(root)
      return res
