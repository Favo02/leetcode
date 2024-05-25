from typing import List

class Solution:
  def duplicateNumbersXOR(self, nums: List[int]) -> int:

    double = []
    seen = set()

    for n in nums:
      if n in seen:
        double.append(n)
      else:
        seen.add(n)

    if len(double) == 0:
      print(0)
      return 0

    res = double[0]
    for d in double[1:]:
      res ^= d

    print(res)
    return res

s = Solution()
s.duplicateNumbersXOR([1,2,1,3])
s.duplicateNumbersXOR([1,2,3])
s.duplicateNumbersXOR([1,2,2,1])
