from typing import List
import math

class Solution:
  def minimumReplacement(self, nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)-1, 0, -1):
      if nums[i] < nums[i-1]:
        p = math.ceil(nums[i-1] / nums[i])
        count += p-1
        nums[i-1] = nums[i-1] // p
    print(count)
    return count

s = Solution()
s.minimumReplacement([3,9,3]) # 2
s.minimumReplacement([1,2,3,4,5]) # 0
s.minimumReplacement([12,9,7,6,10]) # 6
s.minimumReplacement([12,9,7,6,17,19,21]) # 6
s.minimumReplacement([368,112,282,349,127,36]) # 39
