# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        lenn = 0
        cur = head
        while cur:
            cur = cur.next
            lenn += 1

        size = lenn // k
        rem = lenn % k

        res = []
        start = head
        cur = head
        for _ in range(k):
            cursize = size
            if rem > 0:
                cursize += 1
                rem -= 1

            for _ in range(cursize-1):
                if not cur:
                    break
                cur = cur.next

            res.append(start)
            if cur:
                start = cur.next
                cur.next = None
            else:
                start = None

            cur = start

        return res
