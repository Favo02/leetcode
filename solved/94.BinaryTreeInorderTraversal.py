# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def dfs(root):
  res = []
  if not root: return res
  res += dfs(root.left)
  res.append(root.val)
  res += dfs(root.right)
  return res

class Solution:
  def inorderTraversal(self, root):
    return dfs(root)
