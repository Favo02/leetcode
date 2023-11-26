from typing import List
from collections import deque

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:

    sl = []
    stack = deque()
    for i,h in enumerate(heights):
      while stack and heights[stack[-1]] >= h:
        stack.pop()
      if not stack:
        sl.append(-1)
      else:
        sl.append(stack[-1])
      stack.append(i)

    sr = []
    stack = deque()
    for i,h in enumerate(list(reversed(heights))):
      while stack and heights[-stack[-1]-1] >= h:
        stack.pop()
      if not stack:
        sr.append(-1)
      else:
        sr.append(len(heights) - stack[-1]-1)
      stack.append(i)
    sr = list(reversed(sr))

    Max = 0
    for i,h in enumerate(heights):
      limitl = 0 if sl[i] == -1 else sl[i]+1
      limitr = len(heights) if sr[i] == -1 else sr[i]
      area = h * (limitr-limitl)
      Max = max(Max, area)

    print(Max)
    return Max

s = Solution()
s.largestRectangleArea([2,1,5,6,2,3]) # 10
s.largestRectangleArea([2,4]) # 4
s.largestRectangleArea([0]) # 0
s.largestRectangleArea([1]) # 1
s.largestRectangleArea([1,2,3,4,5]) # 9
s.largestRectangleArea([2,0,2]) # 2
s.largestRectangleArea([1,3,2,4,4,2])
