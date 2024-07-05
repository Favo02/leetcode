# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head.next
        cur = head.next
        cursum = 0

        while cur:

            if cur.val == 0:
                prev.val = cursum
                prev.next = cur.next
                prev = prev.next
                cursum = 0
            else:
                cursum += cur.val

            cur = cur.next

        return head.next
