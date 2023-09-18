from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    notdup = set()
    for i in nums:
      if i in notdup:
        notdup.remove(i)
      else:
        notdup.add(i)
    res = notdup.pop()
    print(res)
    return res

s = Solution()
s.singleNumber([2,2,1])
s.singleNumber([4,1,2,1,2])
s.singleNumber([1])
