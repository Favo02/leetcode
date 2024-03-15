from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:

    prefix = [1]
    suffix = [1]

    pre = nums[0]
    suf = nums[-1]

    p = 1
    s = -2

    for _ in range(len(nums)-1):
      prefix.append(pre)
      pre *= nums[p]
      p += 1

      suffix.append(suf)
      suf *= nums[s]
      s -= 1

    return [p * s for p,s in zip(prefix, reversed(suffix))]

s = Solution()
s.productExceptSelf([1,2,3,4]) # [24,12,8,6]
s.productExceptSelf([-1,1,0,-3,3]) # [0,0,9,0,0]
