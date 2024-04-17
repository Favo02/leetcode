class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

    q = deque([(root, '')])
    res = None

    while q:
      node, string = q.popleft()
      string = chr(node.val + ord('a')) + string

      if not node.left and not node.right:
        res = string if res is None else min(res, string)
        continue

      if node.left:
        q.append((node.left, string))
      if node.right:
        q.append((node.right, string))

    return res
