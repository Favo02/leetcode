# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        first_crit = None
        last_crit = None
        max_dist = float("inf")
        crit = 0

        i = 1
        prev = head
        cur = head.next

        while cur.next:

            if (prev.val > cur.val < cur.next.val) or (prev.val < cur.val > cur.next.val):
                crit += 1
                if first_crit is None:
                    first_crit = i
                if last_crit is not None:
                    max_dist = min(max_dist, i - last_crit)
                last_crit = i

            prev = cur
            cur = cur.next
            i += 1

        if crit < 2:
            return [-1, -1]

        return [max_dist, last_crit-first_crit]
