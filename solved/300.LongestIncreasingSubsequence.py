class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dp = []
    for n in nums:
      greather = [d+1 for j, d in enumerate(dp) if n > nums[j]]
      if len(greather) > 0:
        dp.append(max(greather))
      else:
        dp.append(1)
    return max(dp)
