from typing import List

class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    count = 0
    found = {}
    for n in nums:
      if n in found:
        count += found[n]
        found[n] += 1
      else:
        found[n] = 1
    print(count)
    return count

s = Solution()
s.numIdenticalPairs([1,2,3,1,1,3])
s.numIdenticalPairs([1,1,1,1])
s.numIdenticalPairs([1,2,3])
