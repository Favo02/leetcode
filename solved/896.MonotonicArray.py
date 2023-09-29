from typing import List

class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    inc = True
    dec = True
    for i in range(len(nums)-1):
      if nums[i+1] < nums[i]: inc = False
      if nums[i+1] > nums[i]: dec = False
      if not dec and not inc: break
    return inc or dec

s = Solution()
print(s.isMonotonic([1,2,2,3]))
print(s.isMonotonic([6,5,4,4]))
print(s.isMonotonic([1,3,2]))
