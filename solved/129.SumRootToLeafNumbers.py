from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(root, num):
      next = num*10 + root.val
      if (not root.left) and (not root.right):
        return next
      l = dfs(root.left, next) if root.left else 0
      r = dfs(root.right, next) if root.right else 0
      return l + r

    return dfs(root, 0)

s = Solution()
print(s.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
print(s.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
