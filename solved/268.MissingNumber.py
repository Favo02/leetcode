from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    temp = [-1] * (len(nums)+1)

    for n in nums:
      temp[n] = n
    for i, n in enumerate(temp):
      if n == -1:
        print(i)
        return i
