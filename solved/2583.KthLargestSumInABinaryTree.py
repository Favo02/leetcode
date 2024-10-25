# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = defaultdict(int)
        queue = deque([(0, root)])

        while queue:
            curlev, cur = queue.popleft()
            levels[curlev] += cur.val
            if cur.left: queue.append((curlev+1, cur.left))
            if cur.right: queue.append((curlev+1, cur.right))

        res = sorted(levels.values(), reverse=True)
        return res[k-1] if k <= len(res) else -1
