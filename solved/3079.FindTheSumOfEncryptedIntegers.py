from typing import List

class Solution:
  def sumOfEncryptedInt(self, nums: List[int]) -> int:
    return sum([int(max(str(n))*len(str(n))) for n in nums])

s = Solution()
s.sumOfEncryptedInt([1,2,3])
s.sumOfEncryptedInt([10,21,31])
