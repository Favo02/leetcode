# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        levels = []
        sum_levels = []

        queue = deque([(0, root)])
        while queue:
            lvl, cur = queue.popleft()

            if lvl >= len(levels):
                levels.append([cur])
                sum_levels.append(cur.val)
            else:
                levels[lvl].append(cur)
                sum_levels[lvl] += cur.val

            if cur.left: queue.append((lvl + 1, cur.left))
            if cur.right: queue.append((lvl + 1, cur.right))

        queue = deque([(0, root)])
        while queue:
            lvl, cur = queue.popleft()

            if lvl == 0:
                cur.val = 0

            childsum = 0
            if cur.left: childsum += cur.left.val
            if cur.right: childsum += cur.right.val

            if cur.left:
                cur.left.val = sum_levels[lvl+1] - childsum
                queue.append((lvl + 1, cur.left))
            if cur.right:
                cur.right.val = sum_levels[lvl+1] - childsum
                queue.append((lvl + 1, cur.right))

        return root
