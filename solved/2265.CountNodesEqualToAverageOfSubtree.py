# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def avgSubtree(root):
  queue = [root]
  count = 0
  res = 0
  while queue:
    cur = queue.pop(0)
    res += cur.val
    count += 1
    if cur.left: queue.append(cur.left)
    if cur.right: queue.append(cur.right)
  return res // count


class Solution:
  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    queue = [root]
    res = []
    while queue:
      cur = queue.pop(0)
      if cur.left: queue.append(cur.left)
      if cur.right: queue.append(cur.right)

      if cur.val == avgSubtree(cur):
        res.append(cur.val)
    print(res)
    return len(res)
