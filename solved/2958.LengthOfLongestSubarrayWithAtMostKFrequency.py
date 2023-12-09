from typing import List

class Solution:
  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    F = {}
    end = [0] * len(nums)
    start = 0
    for i,n in enumerate(nums):
      F[n] = F.get(n, 0) + 1

      while F.get(n, 0) > k:
        F[nums[start]] -= 1
        start += 1

      end[i] = i-start

    print(max(end)+1)
    return max(end)+1

s = Solution()
s.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2) # 6
s.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1) # 2
s.maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4) # 4
