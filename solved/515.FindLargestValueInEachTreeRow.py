# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    res = []

    lastRow = [root]
    while lastRow:
      maxV = None
      newRow = []
      for elem in lastRow:
        if maxV is None:
          maxV = elem.val
        else:
          maxV = max(maxV, elem.val)
        if elem.left:
          newRow.append(elem.left)
        if elem.right:
          newRow.append(elem.right)
      res.append(maxV)
      lastRow = newRow
    return res

