class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    return sum([f for f in Counter(nums).values() if f == max(Counter(nums).values())])
