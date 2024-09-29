from typing import List

class Solution:
  def maximumTotalSum(self, maximumHeight: List[int]) -> int:

    maximumHeight.sort(reverse=True)

    res = 0
    last = float('inf')

    for m in maximumHeight:
      cur = min(last-1, m)
      if cur == 0:
        print(-1)
        return -1

      res += cur
      last = cur

    print(res)
    return res







s = Solution()
s.maximumTotalSum([2,3,4,3])
s.maximumTotalSum([15,10])
s.maximumTotalSum([2,2,1])
