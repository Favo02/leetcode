from typing import List

class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    res = [0 for _ in nums]

    suml = 0
    for i,n in enumerate(nums):
      res[i] += n*i - suml
      suml += n

    sumr = 0
    for i,n in enumerate(reversed(nums)):
      sumr += n
      res[-i-1] += sumr - n*(i+1)

    print(res)
    return res

s = Solution()
s.getSumAbsoluteDifferences([2,3,5]) # [4,3,5]
