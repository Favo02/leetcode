# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur = head
    len = 0
    while cur is not None:
      cur = cur.next
      len += 1

    if n == len:
      return head.next

    cur = head
    for _ in range(len-n-1):
      cur = cur.next
    else:
      cur.next = cur.next.next if cur.next else None
    return head
