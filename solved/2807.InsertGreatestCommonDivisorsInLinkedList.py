# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        while cur and cur.next:
            n, m = cur.val, cur.next.val
            new = ListNode(math.gcd(n, m), cur.next)
            cur.next = new
            cur = new.next

        return head
