from typing import List
from collections import deque

class Solution:
  def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:

    summ = sum(nums)

    queue = deque(sorted(enumerate(nums), key=lambda x: x[1]))
    marked = set()

    res = []

    for tomark, qty in queries:
      if tomark not in marked:
        marked.add(tomark)
        summ -= nums[tomark]

      while qty > 0 and queue:
        i, n = queue.popleft()
        if i in marked:
          continue

        marked.add(i)
        summ -= n
        qty -= 1

      res.append(summ)

    return res

s = Solution()
print(s.unmarkedSumArray([1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]))
print(s.unmarkedSumArray([1,4,2,3], queries = [[0,1]]))
