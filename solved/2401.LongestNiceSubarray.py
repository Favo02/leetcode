from typing import List

class Solution:
  def longestNiceSubarray(self, nums: List[int]) -> int:

    bits = 0

    start = 0
    res = 1

    for end, n in enumerate(nums):
      while bits & n != 0:
        bits ^= nums[start]
        start += 1
        assert start <= end
      bits |= n
      res = max(res, end-start+1)

    return res

s = Solution()
print(s.longestNiceSubarray([1,3,8,48,10]))
print(s.longestNiceSubarray([3,1,5,11,13]))
print(s.longestNiceSubarray([1,4,8,5,2]))
