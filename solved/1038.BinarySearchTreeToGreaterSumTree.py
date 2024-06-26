# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(root, num):
            if not root:
                return 0

            right = root.val + dfs(root.right, num)
            left = dfs(root.left, num + right)
            root.val = num+right
            return right + left

        dfs(root, 0)
        return root
