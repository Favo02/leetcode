# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    occs = {}
    queue = [root]

    while queue:
      cur = queue.pop(0)

      if cur.val in occs: occs[cur.val]+=1
      else: occs[cur.val]=1

      if cur.left: queue.append(cur.left)
      if cur.right: queue.append(cur.right)

    keys = set([root.val])
    value = 1

    for k,v in occs.items():
      if v > value:
        keys = set([k])
        value = v
      elif v == value:
        keys.add(k)

    return keys
