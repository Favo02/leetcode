from typing import List
from collections import defaultdict

class Solution:
  def subarrayAtMostKDistinct(self, nums, k):
    res = 0
    values = defaultdict(int)
    start = 0

    for end in range(0, len(nums)):
      values[nums[end]] += 1

      while len(values) > k:
        values[nums[start]] -= 1
        if values[nums[start]] == 0:
          del values[nums[start]]

        start += 1

      res += end-start+1
    return res

  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    k0 = self.subarrayAtMostKDistinct(nums, k)
    k1 = self.subarrayAtMostKDistinct(nums, k-1)
    print(k0 - k1)
    return k0 - k1

s = Solution()
s.subarraysWithKDistinct([1,2,1,2,3], k = 2)
s.subarraysWithKDistinct([1,2,1,3,4], k = 3)
