from typing import List
from functools import lru_cache

class Solution:
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

    @lru_cache(maxsize=None)
    def solve(i, j):
      if i == len(nums1) or j == len(nums2):
        return 0

      res = solve(i+1, j+1)
      res = max(res, nums1[i] * nums2[j] + res)
      res = max(res, solve(i+1, j))
      res = max(res, solve(i, j+1))

      return res

    res = solve(0, 0)
    if res == 0:
      res = max(min(nums1) * max(nums2), max(nums1) * min(nums2))

    print(res)
    return res

s = Solution()
s.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])
s.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])
s.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])
s.maxDotProduct([-5,-1,-2], [3,3,5,5])
s.maxDotProduct([13,-7,12,-15,-7,8,3,-7,-5,13,-15,-8,5,7,-1,3,-11,-12,2,-12], [-1,13,-4,-2,-13,2,-4,6,-9,13,-8,-3,-9])
