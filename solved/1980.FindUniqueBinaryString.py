from typing import List

class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    nums = [int(n, 2) for n in nums]

    for n in range(2**len(nums)):
      if n not in nums:
        return bin(n)[2:].rjust(len(nums), '0')

s = Solution()
print(s.findDifferentBinaryString(["01","10"]))
print(s.findDifferentBinaryString(["00","01"]))
print(s.findDifferentBinaryString(["111","011","001"]))
