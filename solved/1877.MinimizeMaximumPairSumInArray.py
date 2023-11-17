from typing import List

class Solution:
  def minPairSum(self, nums: List[int]) -> int:
    nums.sort()
    res = 0
    for i in range(len(nums)//2):
      res = max(res, nums[i] + nums[-i-1])
    print(res)
    return res

s = Solution()
s.minPairSum([3,5,2,3])
s.minPairSum([3,5,4,2,4,6])
