from collections import deque
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    queue = deque([(root, 'r')])

    res = 0

    while queue:
      cur, side = queue.popleft()

      if (not cur.left) and (not cur.right):
        if side == 'l':
          res += cur.val

      if cur.left:
        queue.append((cur.left, 'l'))
      if cur.right:
        queue.append((cur.right, 'r'))

    print(res)
    return res
