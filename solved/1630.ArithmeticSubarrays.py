from typing import List

def isValid(nums):
  nums.sort()
  diff = nums[0]-nums[1]
  for i in range(1,len(nums)-1):
    if (nums[i] - nums[i+1]) != diff:
      return False
  return True

class Solution:
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    res = []
    for ll,rr in zip(l,r):
      if isValid(nums[ll:rr+1]):
        res.append(True)
      else:
        res.append(False)
    print(res)
    return res

s = Solution()
s.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
s.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])
