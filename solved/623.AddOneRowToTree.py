# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
      return TreeNode(val, root)

    lastrow = [ root ]
    for _ in range(depth-2):
      newrow = []
      for r in lastrow:
        if r.left:
          newrow.append(r.left)
        if r.right:
          newrow.append(r.right)
      lastrow = newrow

    for r in lastrow:
      r.left = TreeNode(val, left=r.left)
      r.right = TreeNode(val, right=r.right)

    return root
