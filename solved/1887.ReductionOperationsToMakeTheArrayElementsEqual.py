from typing import List
from collections import defaultdict

class Solution:
  def reductionOperations(self, nums: List[int]) -> int:
    freq = defaultdict(int)
    for n in nums:
      freq[n] += 1

    keys = list(freq.keys())
    keys.sort()

    res = 0
    dist = 0

    for n in keys[1:]:
      dist += 1
      res += (dist * freq[n])

    print(res)
    return res

s = Solution()
s.reductionOperations([5,1,3]) # 3
s.reductionOperations([1,1,1]) # 0
s.reductionOperations([1,1,2,2,3]) # 4
