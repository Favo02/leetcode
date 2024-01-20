from typing import List

class Solution:
  def minimumCost(self, nums: List[int]) -> int:
    res = nums[0] + sum(sorted(nums[1:])[:2])
    print(res)
    return res

s = Solution()
s.minimumCost([1,2,3,12])
s.minimumCost([5,4,3])
s.minimumCost([10,3,1,1])
s.minimumCost([1,1,2])
s.minimumCost([1,5,1,6])
