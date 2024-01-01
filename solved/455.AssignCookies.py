from typing import List

class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    res = 0

    g.sort()
    s.sort()

    ig = iss = 0

    while ig < len(g) and iss < len(s):
      if g[ig] <= s[iss]:
        res += 1
        ig+=1
        iss+=1
      else:
        iss+=1

    print(res)
    return res

s = Solution()
s.findContentChildren([1,2,3], [1,1])
s.findContentChildren([1,2], [1,2,3])
s.findContentChildren([10,9,8,7], [5,6,7,8])
