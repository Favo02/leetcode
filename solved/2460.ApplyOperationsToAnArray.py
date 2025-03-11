class Solution:
  def applyOperations(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
      if nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i+1] = 0
    i = 0
    res = [0] * len(nums)
    for n in nums:
      if n > 0:
        res[i] = n
        i += 1
    return res
