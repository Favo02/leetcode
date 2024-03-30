from typing import List

class Solution:
  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

    for length in range(1, len(nums)+1):
      for skip in range(0, len(nums)-length+1):

        value = 0
        for n in nums[skip:skip+length]:
          value |= n

        if value >= k:
          print(length)
          return length

    print(-1)
    return -1

s = Solution()
s.minimumSubarrayLength(nums = [1,2,3], k = 2)
s.minimumSubarrayLength( [2,1,8], k = 10)
s.minimumSubarrayLength( [1,2], k = 0)
