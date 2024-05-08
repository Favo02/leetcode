from typing import List
from functools import reduce

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    return reduce(lambda acc, cur: acc + (cur[1] if cur[0] % 2 == 0 else 0), enumerate(sorted(nums)), 0)

s = Solution()
s.arrayPairSum([6,2,6,5,1,2])
