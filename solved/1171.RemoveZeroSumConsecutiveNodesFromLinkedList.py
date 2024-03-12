from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    res_head = None
    res_cur = None

    while head:
      cur = head
      prefix_sum = 0
      no_zero_prefix = True

      while cur:
        prefix_sum += cur.val
        if prefix_sum == 0:
          head = cur.next
          no_zero_prefix = False
          break
        cur = cur.next

      if no_zero_prefix:
        if res_head is None:
          res_head = ListNode(head.val)
          res_cur = res_head
        else:
          res_cur.next = ListNode(head.val)
          res_cur = res_cur.next
        head = head.next

    return res_head

s = Solution()
s.removeZeroSumSublists(ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))) # [1,2,-3,3,1]
s.removeZeroSumSublists(ListNode(1, ListNode(1, ListNode(1, ListNode(2))))) # [1,1,1,2]
s.removeZeroSumSublists(ListNode(2, ListNode(0))) # [2,0]
