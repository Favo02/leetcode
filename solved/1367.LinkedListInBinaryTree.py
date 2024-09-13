# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(h, r):
            if not h:
                return True
            if not r:
                return False
            if h.val != r.val:
                return False
            return dfs(h.next, r.left) or dfs(h.next, r.right)

        if not root:
            return False

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
