from typing import Optional
from collections import deque

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

    stack = deque()
    while head:
      stack.append(head.val)
      head = head.next

    cur = None
    prev = None
    carriage = 0
    while stack:
      num = stack.pop() * 2 + carriage
      carriage = 0 if num < 10 else (num // 10)
      cur = ListNode(num % 10, prev)
      prev = cur

    if carriage != 0:
      return ListNode(carriage, cur)

    return cur
