from typing import List

class Solution:
  def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

    occs = []
    for i, n in enumerate(nums):
      if n == x:
        occs.append(i)

    res = []
    for q in queries:
      if q > len(occs):
        res.append(-1)
      else:
        res.append(occs[q-1])

    print(res)
    return res

s = Solution()
s.occurrencesOfElement([1,3,1,7], queries = [1,3,2,4], x = 1)
s.occurrencesOfElement( [1,2,3], queries = [10], x = 5)
