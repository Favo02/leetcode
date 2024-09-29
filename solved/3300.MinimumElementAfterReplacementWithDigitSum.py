from typing import List

class Solution:
  def minElement(self, nums: List[int]) -> int:
    nums = map(str, nums)
    res = float('inf')
    for n in nums:
      a = 0
      for d in n:
        a += int(d)
      res = min(res, a)
    print(res)
    return res




s = Solution()
s.minElement( [10,12,13,14])
s.minElement( [1,2,3,4])
s.minElement( [999,19,199])
