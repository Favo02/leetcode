from typing import List
from collections import Counter

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    res = 0
    c = Counter(nums)
    for e, qty in c.items():
      if e < k:
        res += qty
    print(res)
    return res

s = Solution()
s.minOperations(nums = [2,11,10,1,3], k = 10)
s.minOperations(nums = [1,1,2,4,9], k = 1)
s.minOperations(nums = [1,1,2,4,9], k = 9)
