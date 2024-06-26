# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return []

            left = dfs(root.left)
            right = dfs(root.right)

            return left + [root.val] + right

        def tree(nums, first, last):
            if first > last:
                return None

            median = (first + last) // 2
            root = TreeNode(nums[median])
            root.left = tree(nums, first, median-1)
            root.right = tree(nums, median + 1, last)
            return root

        nums = dfs(root)
        tree = tree(nums, 0, len(nums)-1)

        return tree
