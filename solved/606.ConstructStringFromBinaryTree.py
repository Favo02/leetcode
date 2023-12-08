# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def wrap(arr):
  arr.insert(0, '(')
  arr.append(')')
  return arr

def dfs(root):
  res = []
  res.append(str(root.val))

  if root.left:
    res += wrap(dfs(root.left))
  if root.right:
    if not root.left:
      res += wrap([])
    res += wrap(dfs(root.right))

  return res

class Solution:
  def tree2str(self, root) -> str:
    res = "".join(dfs(root))
    print(res)
    return res

s = Solution()
s.tree2str(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)))

#    1
#   2 3
#  4
# "1(2(4))(3)"
